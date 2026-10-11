# Personal Writing 0.3.6

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

Claude Code는 아래 설치 절차로 등록한 뒤 사용합니다. 로컬 수정본을 일시적으로 시험할 때는 이 폴더를 플러그인 루트로 지정합니다. 복제 저장소 루트에는 기존 humanize-korean 패키지가 남아 있습니다.

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

원본 `install.sh`는 humanize-korean 설치용이므로 이 묶음 설치에 사용하지 않습니다. 사용자 범위 설치와 재설치는 아래 절차를 따르세요. 저장소를 수정하거나 push하는 것만으로 설치된 복사본이 갱신되지는 않습니다.

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

PPTX 디자인/렌더링은 포함하지 않습니다. 실제 발표 시간과 국내 직무별 자기소개서 적합성은 실무 자료로 추가 검증해야 합니다. 모델 교정 품질의 합성 사례 평가 범위는 아래 보고서에 기록합니다. 전용 타입은 원본 산문 점수·light/standard/heavy 게이트를 호출하지 않습니다.

파생 원본: epoko77-ai/im-not-ai, commit `2f3d943d08056b612a92e12bfb72ea94dd2acd18`. MIT 고지는 [LICENSE](LICENSE)에 보존합니다. [초기 개선 보고서](../../TEAM-WRITING-REVIEW.md).

## 실제 모델 평가 (2026-10-11)

Sol 6.1(`gpt-6.1-sol`)과 Opus 5.5(`claude-opus-5-5`)를 실제 실행하며 개선했습니다. 인과 추가, 복합 추측 축약, 사건·인원·날짜의 범위 변경, 오래된 글자 수 보고, 미확인 평균 추론을 발견해 보강했습니다.

[현재 버전의 결과·검증 범위](../../evals/2026-10-11-v036-release/REPORT.md)와 [초기 실패 기록](../../evals/2026-10-11-sol61-opus55/REPORT.md)을 함께 공개합니다. 전체 평가를 최종 버전 한 번의 통과 수치로 합산하지 않습니다. 합성 입력과 명시적 스킬 호출 평가이며, 실무 전반 품질이나 자동 탐색을 보장하지 않습니다.

## 설치와 업데이트

### Claude Code 사용자 범위 설치

```sh
claude plugin install personal-writing --marketplace sangwookp9591/im-not-ai-by-ai-ng --scope user
claude plugin list
```

대화창에서는 다음 명령으로 설치할 수 있습니다.

```text
/plugin marketplace add sangwookp9591/im-not-ai-by-ai-ng
/plugin install personal-writing@im-not-ai-by-ai-ng
```

기존 원본 대신 커스텀 스킬만 사용하려면 설치 성공을 확인한 뒤 원본을 비활성화합니다. 원본이 설치되어 있을 때만 실행합니다.

```sh
claude plugin disable humanize-korean@im-not-ai --scope user
```

업데이트할 때는 마켓플레이스를 새로 받은 뒤 플러그인을 갱신합니다.

```sh
claude plugin marketplace update im-not-ai-by-ai-ng
claude plugin update personal-writing@im-not-ai-by-ai-ng --scope user
claude plugin list
```

설치·갱신 후 Claude Code를 다시 시작합니다. 목록에서 `personal-writing@im-not-ai-by-ai-ng`의 버전과 활성 상태를 확인하세요. 동일 플러그인을 설치한 상태에서 `--plugin-dir`로 중복 로드하지 마세요.

### Codex 사용자 범위 설치·재설치

Codex의 `skill-installer`에 이 저장소의 `extensions/personal-writing/skills/` 아래 6개 폴더를 모두 설치하도록 요청합니다. 기본 위치는 `$CODEX_HOME/skills`이며, 환경 변수가 없으면 `~/.codex/skills`입니다. Orca의 계정별 CODEX_HOME을 사용하는 경우 해당 계정에 설치됩니다.

설치 도우미를 직접 실행할 경우, `<skill-installer>`를 현재 환경의 skill-installer 폴더 경로로 바꿉니다.

```sh
python3 <skill-installer>/scripts/install-skill-from-github.py \
  --repo sangwookp9591/im-not-ai-by-ai-ng \
  --path extensions/personal-writing/skills/my-writing-base \
         extensions/personal-writing/skills/my-planning \
         extensions/personal-writing/skills/my-slides \
         extensions/personal-writing/skills/my-presentation \
         extensions/personal-writing/skills/my-speech \
         extensions/personal-writing/skills/my-application
```

팀원 모두 동일한 버전을 사용하려면 `--ref <검증된 커밋 SHA>`를 추가합니다. Python 인증서 문제로 다운로드가 실패하면 인증서 검증을 끄지 말고 `--method git`을 사용합니다.

도우미는 기존 대상 폴더를 덮어쓰지 않습니다. 재설치 전 기존 6개 폴더를 스킬 탐색 경로 밖으로 백업하고, 같은 커밋에서 6개 모두 다시 설치하세요. 로컬에서 규칙을 수정했다면 백업과 저장소의 차이를 먼저 확인합니다. 설치 후 다음 턴부터 사용할 수 있습니다.

설치 확인 항목:

- 기본 1개와 파생 5개가 같은 부모 폴더 아래에 있는지 확인합니다.
- 각 `SKILL.md`와 `my-writing-base/references/core.md`가 존재하는지 확인합니다.
- 설치본 파일을 선택한 커밋의 원본과 비교합니다. 폴더 존재만으로 최신 버전이라고 판단하지 않습니다.
- 다른 계정이나 프로젝트에 같은 이름의 오래된 설치본이 있으면 해당 환경에서도 별도로 갱신합니다.
