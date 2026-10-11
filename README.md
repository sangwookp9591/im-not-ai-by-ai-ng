# im-not-ai-by-ai-ng

im-not-ai에서 파생한 **Personal Writing 0.3.6**입니다. 한국어 글의 의미와 사실을 보존하면서 AI 특유의 상투적 표현을 다듬습니다. 공통 기본 규칙과 용도별 파생 스킬을 개인·팀 환경에서 함께 사용합니다.

## 기본 → 용도별 스킬

| 스킬 | 사용 목적 |
|---|---|
| `my-writing-base` | 공통 규칙·일반 윤문·용도 선택 |
| `my-planning` | 기획안·요구사항 문서 |
| `my-slides` | PPT 화면에 들어갈 문구 |
| `my-presentation` | 프레젠테이션 전체 흐름 |
| `my-speech` | 말로 전달할 발표 대본 |
| `my-application` | 자기소개서 |

파생 스킬은 기본의 `references/core.md`와 각자의 `references/rules.md`를 읽습니다. 공통 규칙은 한 곳에서 관리합니다. PPTX 제작·디자인·렌더링 기능은 포함하지 않습니다.

## Claude Code 설치

터미널에서 사용자 범위로 설치합니다.

```sh
claude plugin install personal-writing --marketplace sangwookp9591/im-not-ai-by-ai-ng --scope user
```

기존 원본을 커스텀 플러그인으로 교체하는 경우, 설치 성공 후 원본만 비활성화합니다.

```sh
claude plugin disable humanize-korean@im-not-ai --scope user
claude plugin list
```

Claude Code를 다시 시작한 뒤 `/personal-writing:my-planning`처럼 호출합니다. 업데이트 명령과 대화창 설치 방법은 [패키지 안내](extensions/personal-writing/README.md#설치와-업데이트)에 있습니다.

## Codex 설치

Codex에 다음과 같이 요청합니다. **6개 폴더를 모두 같은 스킬 디렉터리에 설치**해야 공통 규칙 참조가 유지됩니다.

```text
skill-installer로 sangwookp9591/im-not-ai-by-ai-ng 저장소의
extensions/personal-writing/skills 아래 my-writing-base, my-planning,
my-slides, my-presentation, my-speech, my-application을 모두 설치해줘.
```

기본 설치 위치는 `$CODEX_HOME/skills`이며, CODEX_HOME이 없으면 `~/.codex/skills`입니다. Orca에서는 현재 계정의 CODEX_HOME을 사용합니다. 설치한 스킬은 다음 턴부터 사용할 수 있습니다.

```text
$my-planning 요구사항 ID와 의무·예외를 유지하면서 말투만 교정해줘.
```

재설치할 때는 기존 커스텀 스킬을 백업한 뒤 6개를 함께 교체합니다. 자세한 설치·수정·검증 방법은 [개인 패키지 README](extensions/personal-writing/README.md)를 참고하세요.

## 품질 평가와 관리

- [공통 기본 스킬](extensions/personal-writing/skills/my-writing-base/SKILL.md)
- [개선 검토 보고서](TEAM-WRITING-REVIEW.md)
- [실제 Sol 6.1·Opus 5.5 평가와 한계](evals/2026-10-11-v036-release/REPORT.md)
- [원본 README 보관본](README.upstream.md)

합성 사례와 명시적 호출로 평가했습니다. 실무 전반의 품질이나 자동 스킬 선택을 보장하지 않습니다. 실제 발표 시간과 직무별 자기소개서 적합성은 사용자 자료로 추가 확인해야 합니다.

원본 코드는 비교용으로 보존합니다. **루트 `install.sh`와 루트 플러그인 대신 `extensions/personal-writing`을 설치하세요.** 기존 INSTALL.md 등 루트 설치 문서는 원본 패키지 안내입니다. 커스텀 패키지는 이 문서와 개인 패키지 README를 기준으로 사용합니다.

평가 결과·메타데이터는 저장소에 보존하며, CLI 원시 trace와 stderr는 세션/컴퓨터 정보가 포함될 수 있어 로컬 평가 폴더에만 보관합니다.
