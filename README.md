<h1 align="center">🌱 Daily Algo</h1>

<p align="center">
  <b>하루 한 문제, 배움을 차곡차곡.</b><br />
  알고리즘 문제를 풀고, 풀이 과정에서 배운 점을 기록합니다.
</p>

<p align="center">
  <img src=".github/assets/readme-badges.svg" width="250" height="28" alt="Python 3 · Programmers" />
</p>

<p align="center">
  <a href="#풀이-목록">풀이 목록</a> ·
  <a href="#기록-방식">기록 방식</a> ·
  <a href="#폴더-구조">폴더 구조</a>
</p>

---

## 풀이 목록

문제명을 누르면 풀이 노트로, **Python**을 누르면 코드로 이동합니다. 풀이 키워드는 저장된 코드의 접근 방식을 기준으로 정리합니다.

| 번호 | 문제 | 풀이 키워드 | 코드 |
| :---: | :--- | :--- | :---: |
| 12906 | [같은 숫자는 싫어](programmers/12906/README.md) | 큐 | [Python](programmers/12906/solution.py) |
| 12909 | [올바른 괄호](programmers/12909/README.md) | 스택 | [Python](programmers/12909/solution.py) |
| 42576 | [완주하지 못한 선수](programmers/42576/README.md) | 해시 | [Python](programmers/42576/solution.py) |
| 42577 | [전화번호 목록](programmers/42577/README.md) | 정렬 · 접두어 비교 | [Python](programmers/42577/solution.py) |
| 42578 | [의상](programmers/42578/README.md) | 해시 · 경우의 수 | [Python](programmers/42578/solution.py) |
| 42586 | [기능개발](programmers/42586/README.md) | 큐 · 시뮬레이션 | [Python](programmers/42586/solution.py) |
| 42748 | [K번째수](programmers/42748/README.md) | 정렬 · 슬라이싱 | [Python](programmers/42748/solution.py) |
| 42840 | [모의고사](programmers/42840/README.md) | 완전탐색 · 나머지 연산 | [Python](programmers/42840/solution.py) |
| 42862 | [체육복](programmers/42862/README.md) | 탐욕법 · 집합 | [Python](programmers/42862/solution.py) |
| 43165 | [타겟 넘버](programmers/43165/README.md) | 깊이 우선 탐색(DFS) · 재귀 | [Python](programmers/43165/solution.py) |

## 기록 방식

정답 코드와 함께 **왜 이렇게 풀었는지**를 남깁니다. 각 문제의 풀이 노트는 다음 내용을 담습니다.

- **문제 이해** — 문제 요약, 원문 링크, 간단한 예시
- **핵심 아이디어** — 사용한 자료구조와 알고리즘, 접근 이유
- **풀이 과정** — 코드 흐름과 시간·공간 복잡도

## 폴더 구조

프로그래머스 문제는 `programmers/문제번호/`에 정리합니다.

```text
daily-algo/
├── README.md                 # 저장소 소개와 풀이 목록
└── programmers/
    └── 문제번호/
        ├── README.md         # 문제 요약과 풀이 노트
        └── solution.py       # Python 풀이
```
