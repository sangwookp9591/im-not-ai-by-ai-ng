#!/usr/bin/env python3
"""Summarize completed runs and local tool traces, never grade writing quality.

Usage: python3 evals/collect_evidence.py evals/<round>
Raw traces stay local. The published summary records only aggregate evidence.
"""
import hashlib
import json
from pathlib import Path
import statistics
import sys


def collect(root):
    cases = json.loads((root / 'cases.json').read_text())
    hashes = json.loads((root / 'snapshot-sha256.json').read_text())
    mismatches = [name for name, digest in hashes.items()
                  if hashlib.sha256((root / 'snapshot' / name).read_bytes()).hexdigest() != digest]
    out = {'snapshot_files': len(hashes), 'snapshot_mismatches': mismatches,
           'unique_inputs': len({(c['request'], c['source']) for c in cases}),
           'providers': {}}
    for provider in ('sol', 'opus'):
        rows = []
        for case in cases:
            work = root / 'runs' / provider / case['id']
            meta = json.loads((work / 'metadata.json').read_text())
            final = (work / 'final.md').read_text()
            core_read = False
            stats_called = False
            trace = work / 'trace.jsonl'
            pending = {}
            if trace.exists():
                for line in trace.read_text().splitlines():
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if provider == 'sol':
                        item = event.get('item', {})
                        if event.get('type') == 'item.completed' and item.get('type') == 'command_execution':
                            cmd = item.get('command', '')
                            if item.get('exit_code') == 0:
                                core_read |= 'core.md' in cmd and '공통 글쓰기 계약' in item.get('aggregated_output', '')
                                stats_called |= 'text_stats.py' in cmd
                    else:
                        for block in event.get('message', {}).get('content', []):
                            if not isinstance(block, dict):
                                continue
                            if block.get('type') == 'tool_use':
                                pending[block['id']] = block
                            if block.get('type') == 'tool_result':
                                call = pending.get(block.get('tool_use_id'), {})
                                args = json.dumps(call.get('input', {}), ensure_ascii=False)
                                content = str(block.get('content', ''))
                                core_read |= 'core.md' in args and '공통 글쓰기 계약' in content and '외부 원문을 결과에 길게 복사하지 않는다' in content
                                stats_called |= 'text_stats.py' in args and not block.get('is_error')
            rows.append(dict(case_id=case['id'], repeat_of=case.get('repeat_of'),
                             success=meta['returncode'] == 0 and meta['has_final'] and not meta.get('is_error', False),
                             requested_model=meta['requested_model'],
                             returned_model_ids=list(meta.get('model_usage', {})),
                             seconds=meta['elapsed_seconds'], response_chars=len(final),
                             core_read_confirmed=core_read if trace.exists() else None,
                             stats_tool_success=stats_called if trace.exists() else None,
                             api_list_cost_usd=meta.get('api_list_cost_usd')))
        first14 = [r for r in rows if int(r['case_id']) <= 14]
        out['providers'][provider] = dict(
            runs=len(rows), successful=sum(r['success'] for r in rows),
            mean_seconds=statistics.mean(r['seconds'] for r in rows),
            original14_case_count=len(first14),
            original14_mean_response_chars=statistics.mean(r['response_chars'] for r in first14) if len(first14) == 14 else None,
            mean_response_chars=statistics.mean(r['response_chars'] for r in rows),
            core_reads_confirmed=sum(r['core_read_confirmed'] is True for r in rows),
            api_list_cost_usd=sum(r['api_list_cost_usd'] or 0 for r in rows) if provider == 'opus' else None,
            records=rows)
    (root / 'execution-summary.json').write_text(json.dumps(out, ensure_ascii=False, indent=2))
    return out


if __name__ == '__main__':
    result = collect(Path(sys.argv[1]))
    print(json.dumps({key: value for key, value in result.items() if key != 'providers'}, ensure_ascii=False))
    for provider, result in result['providers'].items():
        print(provider, json.dumps({key: value for key, value in result.items() if key != 'records'}, ensure_ascii=False))
