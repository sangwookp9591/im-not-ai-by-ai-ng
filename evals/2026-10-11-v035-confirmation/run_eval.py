#!/usr/bin/env python3
"""Run fixed cases in fresh CLI sessions; preserve prompts, traces and results."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent
MODELS = {'sol': 'gpt-6.1-sol', 'opus': 'claude-opus-5-5'}


def run(case, provider):
    work = ROOT / 'runs' / provider / case['id']
    work.mkdir(parents=True, exist_ok=True)
    skill = ROOT / 'snapshot/skills' / case['skill'] / 'SKILL.md'
    prompt = (
        f"다음 스킬을 실제로 읽고 사용해 사용자의 요청을 처리하세요: {skill}\n"
        "스킬이 참조하는 공통 계약과 관련 용도 규칙도 파일에서 읽으세요. "
        "스킬 파일은 수정하지 마세요. 필요하면 현재 작업 폴더에 본문 파일을 작성하고 길이 도구를 실행하세요. "
        "외부 검색이나 다른 에이전트 호출은 하지 마세요. 최종 응답에 사용자에게 전달할 결과를 포함하세요.\n\n"
        f"사용자 요청:\n{case['request']}\n\n교정 대상 원문:\n{case['source']}\n"
    )
    if case.get('prompt_override'):
        prompt = case['prompt_override']
    (work / 'prompt.txt').write_text(prompt)
    if provider == 'sol':
        cmd = ['codex', '--no-daemon', 'exec', '--model', MODELS[provider],
               '-c', 'model_reasoning_effort="medium"', '--sandbox', 'workspace-write',
               '--ephemeral', '--skip-git-repo-check', '--json',
               '--output-last-message', str(work / 'final.md'), '-']
    else:
        cmd = ['claude', '-p', '--model', MODELS[provider], '--effort', 'medium',
               '--output-format', 'stream-json', '--verbose', '--no-session-persistence',
               '--tools', 'Read,Bash,Write', '--allowedTools', 'Read,Bash,Write',
               '--permission-mode', 'dontAsk', '--strict-mcp-config', '--setting-sources', '',
               '--add-dir', str(ROOT / 'snapshot')]
    started = datetime.now(timezone.utc).isoformat()
    start = time.monotonic()
    timed_out = False
    try:
        result = subprocess.run(cmd, input=prompt, cwd=work, text=True, capture_output=True, timeout=300)
        stdout, stderr, code = result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as error:
        def decode(value):
            return value.decode(errors='replace') if isinstance(value, bytes) else (value or '')
        stdout, stderr, code = decode(error.stdout), decode(error.stderr), None
        timed_out = True
    (work / 'trace.jsonl').write_text(stdout)
    (work / 'stderr.txt').write_text(stderr)
    events = []
    for line in stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    metadata = dict(case_id=case['id'], provider=provider, requested_model=MODELS[provider],
                    effort='medium', command=cmd, started_at=started,
                    elapsed_seconds=round(time.monotonic()-start, 3), returncode=code,
                    timed_out=timed_out)
    if provider == 'opus':
        results = [event for event in events if event.get('type') == 'result']
        if results:
            end = results[-1]
            (work / 'final.md').write_text(end.get('result', ''))
            metadata.update(is_error=end.get('is_error'), usage=end.get('usage'),
                            model_usage=end.get('modelUsage'), permission_denials=end.get('permission_denials'),
                            api_list_cost_usd=end.get('total_cost_usd'))
    else:
        endings = [event for event in events if event.get('type') == 'turn.completed']
        if endings:
            metadata['usage'] = endings[-1].get('usage')
    metadata['has_final'] = (work / 'final.md').exists() and bool((work / 'final.md').read_text().strip())
    (work / 'metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2))
    print(json.dumps({key: metadata.get(key) for key in ['provider','case_id','returncode','has_final','is_error','elapsed_seconds']}, ensure_ascii=False), flush=True)
    return metadata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--cases', nargs='*')
    parser.add_argument('--review', action='store_true')
    parser.add_argument('--review-id', default='review')
    args = parser.parse_args()
    cases = json.loads((ROOT / 'cases.json').read_text())
    if args.review:
        cases = [dict(id=args.review_id, skill='my-writing-base', request='', source='',
                      prompt_override=(ROOT / 'review-prompt.txt').read_text())]
    if args.cases:
        cases = [case for case in cases if case['id'] in args.cases]
    metadata = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = []
        for case in cases:
            for provider in MODELS:
                target = ROOT / 'runs' / provider / case['id'] / 'metadata.json'
                if target.exists():
                    raise RuntimeError(f'Refusing to overwrite existing run: {target}')
                futures.append(pool.submit(run, case, provider))
        for future in as_completed(futures):
            metadata.append(future.result())
    (ROOT / 'last-batch.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
