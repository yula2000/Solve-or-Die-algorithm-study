# 🐣 Git이 처음이라면

> 처음엔 다 어렵습니다. 천천히 읽어보세요 🙂

&nbsp;

## 📖 용어 설명

| 용어 | 설명 |
| :-- | :-- |
| `clone` | 원격 저장소(GitHub)를 내 컴퓨터로 복사해오는 것 |
| `branch` | 독립적으로 작업할 수 있는 공간. 본인 닉네임 브랜치에서만 작업해요 |
| `commit` | 변경사항을 로컬(내 컴퓨터)에 저장하는 것. 일종의 저장 포인트 |
| `push` | 로컬에 저장된 commit을 원격 저장소(GitHub)에 올리는 것 |
| `pull` | 원격 저장소(GitHub)의 최신 내용을 내 컴퓨터로 가져오는 것 |
| `PR` | Pull Request. 내 브랜치를 master에 합쳐달라고 요청하는 것 |
| `merge` | 브랜치를 master에 합치는 것 |

&nbsp;

## ⚙️ 최초 1회 설정

Git을 처음 설치했다면 이름과 이메일을 등록해주세요.

```bash
git config --global user.name "본인이름"
git config --global user.email "GitHub 이메일"
```

&nbsp;

## ⚡ 자주 하는 실수 & 해결법

### ❌ 실수 1. push했더니 오류가 났어요

```
error: failed to push some refs
```

다른 멤버의 변경사항이 먼저 올라가 있을 때 발생해요. pull을 먼저 하고 push하면 돼요.

```bash
git pull origin 본인닉네임
git push origin 본인닉네임
```

&nbsp;

### ❌ 실수 2. master 브랜치에서 작업해버렸어요

내 브랜치가 아닌 `master`에서 실수로 작업한 경우, 아래 순서대로 하면 돼요.

```bash
# 1. 현재 변경사항을 임시 저장
git stash

# 2. 내 브랜치로 이동
git checkout 본인닉네임

# 3. 임시 저장한 변경사항 불러오기
git stash pop

# 4. 이후 정상적으로 add, commit, push
git add .
git commit -m "✨feat: [BOJ] 1000 A+B"
git push origin 본인닉네임
```

&nbsp;

### ❌ 실수 3. 커밋 메시지를 잘못 썼어요

가장 최근 커밋 메시지만 수정할 수 있어요. (push 전에만 가능해요)

```bash
git commit --amend -m "✨feat: [BOJ] 1000 A+B"
```

&nbsp;

### ❌ 실수 4. 지금 내가 어느 브랜치에 있는지 모르겠어요

```bash
git branch
```

현재 브랜치 앞에 `*` 표시가 붙어요. 항상 작업 전에 확인하는 습관을 들이세요!

```bash
# 브랜치 이동
git checkout 본인닉네임
```

&nbsp;

## 💡 흐름 한눈에 보기

```
[내 컴퓨터]                          [GitHub]

  작업
   ↓
git add .
   ↓
git commit -m "..."
   ↓
git push origin 본인닉네임  ------→  본인닉네임 브랜치
                                          ↓
                                       PR 생성
                                          ↓
                                     코드 리뷰
                                          ↓
                                       master에 merge
```

&nbsp;

## 🔗 참고 자료

- [Git 공식 문서 (한국어)](https://git-scm.com/book/ko/v2)
- [누구나 쉽게 이해할 수 있는 Git 입문](https://backlog.com/git-tutorial/kr/)
- [GitHub Docs](https://docs.github.com/ko)
