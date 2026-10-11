# im-not-ai-by-ai-ng

im-not-ai를 복제해 기본 → 용도별 파생 스킬 구조로 확장한 개인 저장소입니다.

개인 패키지는 [extensions/personal-writing](extensions/personal-writing/README.md)에 있습니다. 기본 규칙 한 곳을 공유하고 기획·PPT·프레젠테이션·발표·자기소개서 스킬을 각각 호출합니다.

- [기본 스킬](extensions/personal-writing/skills/my-writing-base/SKILL.md)
- [개선 검토 보고서](TEAM-WRITING-REVIEW.md)
- [Sol 6.1·Opus 5.5 실제 품질 평가](evals/2026-10-11-sol61-opus55/REPORT.md)
- [원본 README](README.upstream.md)

원본 코드는 비교와 개선을 위해 보존합니다. 루트의 기존 설치 스크립트 대신 개인 패키지의 사용 안내를 따르세요. 로컬 복제본이며 아직 원격 배포하지 않았습니다.

## Claude Code 설치

```text
/plugin marketplace add sangwookp9591/im-not-ai-by-ai-ng
/plugin install personal-writing@im-not-ai-by-ai-ng
```

이 저장소의 마켓플레이스는 extensions/personal-writing을 설치합니다. 원본 humanize-korean은 비교용으로 보존되어 있습니다. Codex 설치와 파생 스킬 추가는 [개인 패키지 안내](extensions/personal-writing/README.md)를 참고하세요.

평가 결과·메타데이터는 저장소에 보존하며, CLI 원시 trace와 stderr는 세션/컴퓨터 정보가 포함될 수 있어 로컬 평가 폴더에만 보관합니다.
