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

## 팀원에게 공유하기

팀원에게 [이 저장소 링크](https://github.com/sangwookp9591/im-not-ai-by-ai-ng)와 사용하는 앱에 맞는 아래 설치 방법을 전달하세요. 설치 대상은 **personal-writing**이며, 기본 1개와 파생 5개를 함께 사용합니다.

| 사용하는 환경 | 설치 방법 | 사용 방법 |
|---|---|---|
| Claude 데스크톱 채팅·Cowork | Customize에서 마켓플레이스 추가 | `/`로 스킬 선택 |
| Claude Code | 대화창 명령 또는 터미널 명령 | `/personal-writing:my-planning` 등 |
| Codex 데스크톱 | 대화창에서 skill-installer에 설치 요청 | `$my-planning` 등 |

## Claude 데스크톱 설치

1. 왼쪽 **Customize → Plugins**를 엽니다. Cowork에서는 먼저 Cowork 탭을 선택합니다.
2. **Add → Add marketplace**를 선택합니다.
3. 저장소 입력란에 다음 값을 넣습니다.

   ```text
   sangwookp9591/im-not-ai-by-ai-ng
   ```

4. 추가된 마켓플레이스에서 **personal-writing**을 찾아 **Add**로 설치합니다.
5. 새 대화에서 `/`를 입력하거나 `+` 버튼을 눌러 설치된 스킬을 선택합니다.

플러그인은 Claude 계정에 저장됩니다. 공식 안내 기준 유료 플랜(Pro·Max·Team·Enterprise)에서 지원하며, 조직 정책에 따라 외부 마켓플레이스 추가가 제한될 수 있습니다. 해당 메뉴가 보이지 않거나 저장소가 차단되면 계정 플랜과 조직의 허용 설정을 확인하세요. [Claude 공식 플러그인 안내](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)

**로컬 Claude Code에만 설치한 플러그인이 일반 Claude 채팅 계정으로 업로드되지는 않습니다.** 데스크톱 채팅에서도 쓰려면 위 절차로 계정에 설치하세요. 계정에서 Claude Code로의 동기화는 공식 안내 기준 Claude Code 2.1.273 이상에서 지원하며, 같은 Claude 계정으로 로그인해야 합니다. [계정 동기화 안내](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)

## Claude Code 설치

### 대화창에서 설치

Claude Code 대화창에 다음 명령을 순서대로 입력합니다. 일반 Claude 채팅 입력창용 명령이 아닙니다.

```text
/plugin marketplace add sangwookp9591/im-not-ai-by-ai-ng
/plugin install personal-writing@im-not-ai-by-ai-ng
```

### 터미널에서 설치

Claude Code CLI가 설치되어 있다면 다음 명령으로 사용자 범위에 설치할 수 있습니다. 대화창 설치와 터미널 설치 중 하나만 진행하면 됩니다.

```sh
claude plugin install personal-writing --marketplace sangwookp9591/im-not-ai-by-ai-ng --scope user
claude plugin list
```

기존 `humanize-korean@im-not-ai`를 커스텀 플러그인으로 교체하는 경우에만, 새 플러그인의 설치 성공을 확인한 뒤 원본을 비활성화합니다.

```sh
claude plugin disable humanize-korean@im-not-ai --scope user
```

Claude Code를 다시 시작한 뒤 사용합니다.

```text
/personal-writing:my-planning 이 기획안의 요구사항 ID와 의무·예외를 유지하면서 말투만 교정해줘.
```

## Codex 데스크톱 설치

Codex 데스크톱의 새 대화에 아래 요청을 그대로 붙여넣습니다. **6개 폴더를 모두 같은 스킬 디렉터리에 설치**해야 공통 규칙 참조가 유지됩니다.

```text
skill-installer를 사용해서 다음 GitHub 저장소의 커스텀 스킬을 설치해줘.

저장소: sangwookp9591/im-not-ai-by-ai-ng
경로: extensions/personal-writing/skills/

설치할 스킬:
- my-writing-base
- my-planning
- my-slides
- my-presentation
- my-speech
- my-application

현재 사용자 스킬 디렉터리에 6개를 모두 설치하고,
공통 규칙 참조가 유지되는지 확인해줘.
기존 설치가 있다면 수정 내용을 스킬 탐색 경로 밖에 백업한 뒤 갱신해줘.
```

설치 과정에서 네트워크 접근이나 사용자 스킬 폴더 쓰기 권한을 요청하면 설치 대상과 경로를 확인한 뒤 허용합니다.

기본 설치 위치는 `$CODEX_HOME/skills`이며, CODEX_HOME이 없으면 `~/.codex/skills`입니다. Orca에서는 현재 계정의 CODEX_HOME을 사용합니다. 설치한 스킬은 다음 턴부터 사용할 수 있습니다.

```text
$my-planning 요구사항 ID와 의무·예외를 유지하면서 말투만 교정해줘.
```

## 용도별 호출 예시

Claude 데스크톱 채팅에서는 `/` 메뉴에서 해당 스킬을 선택합니다. Claude Code와 Codex에서는 다음 이름으로 명시적으로 호출할 수 있습니다.

| 용도 | Claude Code | Codex |
|---|---|---|
| 일반 윤문·용도 선택 | `/personal-writing:my-writing-base` | `$my-writing-base` |
| 기획안·요구사항 | `/personal-writing:my-planning` | `$my-planning` |
| PPT 화면 문구 | `/personal-writing:my-slides` | `$my-slides` |
| 프레젠테이션 전체 구성 | `/personal-writing:my-presentation` | `$my-presentation` |
| 발표 대본 | `/personal-writing:my-speech` | `$my-speech` |
| 자기소개서 | `/personal-writing:my-application` | `$my-application` |

호출 뒤에 요청과 원문을 붙입니다. 예를 들어 `$my-slides 아래 슬라이드의 수치와 조건을 유지하면서 화면 문구를 간결하게 교정해줘.`처럼 사용합니다.

## 업데이트·재설치·설치 확인

### Claude Code 업데이트

```sh
claude plugin marketplace update im-not-ai-by-ai-ng
claude plugin update personal-writing@im-not-ai-by-ai-ng --scope user
claude plugin list
```

갱신 후 Claude Code를 다시 시작합니다. 목록에서 `personal-writing@im-not-ai-by-ai-ng`의 버전과 활성 상태를 확인하세요. 이 명령은 로컬 Claude Code 설치본을 갱신합니다. Claude 데스크톱 계정에 설치한 플러그인은 Customize → Plugins에서 별도로 상태를 확인합니다.

### Codex 업데이트·재설치

위 설치 요청을 다시 사용하면 됩니다. 기존 대상이 있으면 설치 도우미가 덮어쓰지 않으므로, 기존 6개 폴더를 스킬 탐색 경로 밖으로 백업한 뒤 함께 교체합니다. 로컬에서 수정한 규칙이 있다면 차이를 먼저 확인하세요.

팀원 모두 같은 버전을 쓰려면 설치 요청에 **“검증된 커밋 SHA를 --ref로 지정해서 6개 모두 같은 커밋에서 설치해줘”**를 추가하고 사용할 SHA를 전달합니다. 버전별 검증 범위는 아래 평가 보고서를 참고하세요.

### 설치 확인과 문제 해결

- **Claude Code:** `claude plugin list`에서 커스텀 플러그인의 활성 상태를 확인합니다.
- **Claude 데스크톱:** Customize → Plugins에서 설치 상태를 확인하고, 새 대화의 `/` 메뉴에서 스킬을 찾습니다.
- **Codex:** 설치된 6개 `SKILL.md`와 `my-writing-base/references/core.md`의 존재 및 원본과의 일치를 확인하도록 요청합니다.
- **공통 규칙 파일을 찾지 못할 때:** 파생 스킬 하나만 설치하지 않았는지 확인하고 6개를 같은 부모 폴더에 설치합니다.
- **다른 계정·프로젝트에서 오래된 규칙이 적용될 때:** 해당 환경에 같은 이름의 별도 설치본이 있는지 확인합니다.
- **Python 인증서 오류로 Codex 설치가 실패할 때:** 인증서 검증을 끄지 말고 설치 도우미의 `--method git` 방식을 사용하도록 요청합니다.

저장소를 수정하거나 push하는 것만으로 팀원의 로컬 설치본이 갱신되지는 않습니다. 자세한 수동 설치·규칙 수정·검증 방법은 [개인 패키지 README](extensions/personal-writing/README.md#설치와-업데이트)를 참고하세요.

## 품질 평가와 관리

- [공통 기본 스킬](extensions/personal-writing/skills/my-writing-base/SKILL.md)
- [개선 검토 보고서](TEAM-WRITING-REVIEW.md)
- [실제 Sol 6.1·Opus 5.5 평가와 한계](evals/2026-10-11-v036-release/REPORT.md)
- [원본 README 보관본](README.upstream.md)

합성 사례와 명시적 호출로 평가했습니다. 실무 전반의 품질이나 자동 스킬 선택을 보장하지 않습니다. 실제 발표 시간과 직무별 자기소개서 적합성은 사용자 자료로 추가 확인해야 합니다.

원본 코드는 비교용으로 보존합니다. **루트 `install.sh`와 루트 플러그인 대신 `extensions/personal-writing`을 설치하세요.** 기존 INSTALL.md 등 루트 설치 문서는 원본 패키지 안내입니다. 커스텀 패키지는 이 문서와 개인 패키지 README를 기준으로 사용합니다.

평가 결과·메타데이터는 저장소에 보존하며, CLI 원시 trace와 stderr는 세션/컴퓨터 정보가 포함될 수 있어 로컬 평가 폴더에만 보관합니다.
