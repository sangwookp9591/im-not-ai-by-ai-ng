# Personal Writing 0.3.0

im-not-ai 복제본에서 관리하는 개인 글쓰기 스킬입니다. 공통 기본 1개와 독립적으로 호출할 수 있는 파생 5개를 제공합니다.

```text
skills/
├── my-writing-base/       공통 계약·일반 윤문·용도 라우팅
│   ├── SKILL.md
│   ├── references/core.md
│   ├── references/sources.md
│   └── scripts/text_stats.py
├── my-planning/           기획안·요구사항
├── my-slides/             PPT 화면 문구
├── my-presentation/       프레젠테이션 전체 흐름
├── my-speech/             발표 대본
└── my-application/        자기소개서
```

각 파생 폴더에는 SKILL.md와 references/rules.md가 있습니다. 런타임의 상속 기능에 의존하지 않고, 파생 스킬이 기본의 `references/core.md`를 먼저 읽도록 명시합니다. 기본의 라우터를 다시 호출하지 않아 순환을 피합니다.

## 사용

Claude Code는 이 폴더를 플러그인 루트로 사용합니다. 복제 저장소 루트에는 기존 humanize-korean 패키지가 남아 있습니다.

```sh
claude --plugin-dir /absolute/path/to/my-writing-skills/extensions/personal-writing
```

| 목적 | Codex | Claude Code |
|---|---|---|
| 기본 윤문/용도 선택 | `$my-writing-base` | `/personal-writing:my-writing-base` |
| 기획 문서 | `$my-planning` | `/personal-writing:my-planning` |
| PPT 문구 | `$my-slides` | `/personal-writing:my-slides` |
| 프레젠테이션 구성 | `$my-presentation` | `/personal-writing:my-presentation` |
| 발표 대본 | `$my-speech` | `/personal-writing:my-speech` |
| 자기소개서 | `$my-application` | `/personal-writing:my-application` |

예: `$my-planning 요구사항 ID와 의무·예외를 유지하면서 말투만 교정해줘.`

Codex에는 **skills 아래 6개 폴더 모두를 함께** 프로젝트의 `.agents/skills/` 또는 개인 스킬 디렉터리에 배치합니다. 기본과 파생 폴더는 형제 관계를 유지해야 합니다. 단일 파생 폴더만 복사하면 불완전한 설치입니다. 같은 이름의 대상이 없는 경우의 프로젝트별 설치 예:

```sh
mkdir -p /absolute/path/to/project/.agents/skills
cp -R /absolute/path/to/my-writing-skills/extensions/personal-writing/skills/. /absolute/path/to/project/.agents/skills/
```

원본 `install.sh`는 humanize-korean 설치용이므로 이 묶음 설치에 사용하지 않습니다. 이번 작업에서 전역 설치나 원격 게시는 실행하지 않았습니다.

## 내 규칙 수정

- 모든 글의 의미 보존·수정 범위·검증: [공통 계약](skills/my-writing-base/references/core.md).
- 특정 용도의 양식·표현·검증: 해당 파생 폴더의 `references/rules.md`.
- 호출 이름과 자동 선택 설명: 해당 `SKILL.md`의 name/description.
- 자료와 한계: [출처 원장](skills/my-writing-base/references/sources.md).

사용자 요청과 제공 양식을 우선하고, 공통 계약의 수정 범위 안에서 용도별 규칙을 적용합니다. 용도 예외가 사실 창작이나 확신도 변경을 허용하지는 않습니다. 개인 말투 예시는 제공받은 경우에만 관련 용도에 반영합니다.

## 파생 스킬 추가

1. 가까운 용도의 파생 폴더를 새 이름으로 복사합니다. 기본 폴더를 복제하지 않습니다.
2. 폴더명과 SKILL.md의 name을 일치시키고 description을 실제 사용 상황에 맞춥니다.
3. 공통 계약 링크를 유지하고 references/rules.md에 새 용도의 차이·보존 요소·검증을 씁니다.
4. 기본 SKILL.md의 라우팅 표와 이 문서의 호출 표에 추가합니다.
5. 출처와 행동 평가 사례를 추가하고 아래 검증을 실행합니다. 기본 규칙 변경 시 모든 타입의 행동 평가도 확인합니다.

## 검증과 범위

플러그인 폴더에서:

```sh
claude plugin validate .
python3 -m unittest discover -s tests -v
```

각 스킬은 skill-creator의 quick_validate.py로도 검증합니다. 구조·참조·길이 검증과 실제 모델의 교정 품질은 별개입니다. 실제 모델 평가 입력은 [behavior-cases.md](tests/behavior-cases.md)에 있습니다.

PPTX 디자인/렌더링은 포함하지 않습니다. 실제 발표 시간, 국내 직무별 자기소개서 적합성, 모델별 교정 품질은 별도 평가가 필요합니다. 전용 타입은 원본 산문 점수·light/standard/heavy 게이트를 호출하지 않습니다.

파생 원본: epoko77-ai/im-not-ai, commit `2f3d943d08056b612a92e12bfb72ea94dd2acd18`. MIT 고지는 [LICENSE](LICENSE)에 보존합니다. [초기 개선 보고서](../../TEAM-WRITING-REVIEW.md).

## 실제 모델 평가 (2026-10-11)

Sol 6.1과 Opus 5.5에 각각 14개 합성 사례를 실제 실행했습니다. Sol은 13개 통과·1개 수정 필요(인과 추가), Opus는 13개 통과·1개 검토 보류(추측 표지 축약)입니다. 스킬 읽기를 명시한 평가이며 자동 탐색·실무 전반 품질 보장은 아닙니다. [전체 보고서와 원문 결과](../../evals/2026-10-11-sol61-opus55/REPORT.md)를 확인하세요.
