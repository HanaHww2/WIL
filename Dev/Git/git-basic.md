# Git CheatSheet를 만들어보자!
## 브랜치 만들고 이동하기
```bash
git branch # 현재 있는 브랜치 확인
git checkout -b <만들고 싶은 브랜치명>
git checkout <이동하고 싶은 브랜치명>
```
#### 메인과 브랜치 합치기
```bash
git checkout main # main 브랜치로 이동
git merge <머지하고 싶은 브랜치> # 머지한 뒤에도 브랜치는 유지된다.
```

## 푸쉬한 이력을 지우고 수정을 원할 때

```bash
git reset <복구하길 원하는 커밋의 해시값>
git push -f
```
- 리셋 옵션은 원하는 대로 한다.
- 다른 사람이 이미 pull한 경우에는 사용해서는 안 된다. 
- 혹은 혼자 관리하는 레포지토리인 경우에만 사용한다.

## 커밋 메세지를 수정하고 싶을 때
#### 최근 커밋이 아닌 과거 커밋 경우
```bash
git rebase -i <수정하길 원하는 커밋 이전 커밋 해시값>
```
- 지정된 커밋 이후의 커밋 목록이 나열된다.
- reword 혹은 r 명령어로 수정하고 싶은 커밋을 지정한다.
- 커밋 메세지가 하나씩 조회되면 수정을 진행하고 저장한다.

#### 최근 커밋인 경우
```bash
git commit --amend
```
#### 푸시한 경우
- 완료 후 `git push -f` 명령어를 통해 원격 레포에 강제 수정을 진행한다.

#### 🧨rebase 사용시 주의사항
- 커밋 히스토리에서 머지 이력이 삭제된다.
  - 즉, 커밋 로그가 깔끔하게? 정리가 된다.
  - 이걸 뭐라고 하더라... squash 인가?
  
## 루트 디렉토리 변경을 원할 때

예를 들어, 여러 레포지토리를 하나로 합치고 싶은 경우

1. 새로운 루트 디렉토리를 원격 저장소와 연결한다.
    
    ```bash
    git init
    git remote add origin <원격레포주소>
    ```
    - HEAD 관련 오류가 났다. 이 것, 저 것 확인해보니, 브랜치가 제대로 조회되지 않았다.
    - 최초 커밋을 하고, main 브랜치를 생성해야 아래 명령어들이 동작하는 것 같다! 
2. 로컬의 디렉토리 내 원하는 경로에 서브트리로 구성할 레포지토리를 지정한다.
   1. 원격 레포가 아니더라도 로컬에 존재하는 git 레포를 지정할 수도 있다. 
    
    ```bash
    git subtree add --prefix=<상대경로> <옮기고 싶은 git 레포>
    ```
    
3. 구성된 디렉토리를 원격에 push한다.
    
    ```bash
    git push origin <원하는 브랜치명>
    ```
    

## 레포지토리 내 서브 디렉토리를 새로운 레포로 만들고 싶을 때

## 원격 브랜치를 로컬로 가져오기

#### 원격 레포 업데이트 하기
```bash
git remote update
```
#### 브랜치 조회하기
```bash
git branch # 로컬 브랜치 목록 조회
git branch -a # 전체 브랜치 목록 조회
git branch -r # 원격 브랜치 목록 조회
```
#### 리모트 브랜치를 로컬에 가져와 브랜치 로컬 만들기
```bash
# 리모트 브랜치 명으로 로컬 내 브랜치 생성
git checkout -t [remote-branch-name]

# 로컬 브랜치 명을 따로 지정하고 싶은 경우
git checkout -b [생성할 branch 이름] [원격 저장소의 branch 이름]
```

#### 리모트 브랜치 참고만 하는 경우
```bash
git checkout [remote-branch-name]
```
- 아무런 옵션없이 원격 저장소의 branch를 checkout 하면 `detached HEAD` 상태로 체크아웃된다.
- 소스를 보고 변경 해볼 수도 있지만 변경사항들은 commit, push 할 수 없으며 다른 branch로 checkout하면 사라진다.

#### 참고 자료
- https://cjh5414.github.io/get-git-remote-branch/
- https://yeniful.tistory.com/57

# git-flow 전략 관련
## rebase
```bash
# 업스트림 레포가 따로 존재하는 경우, 풀리퀘를 머지할 브랜치(develop) 기준
git fetch upstream
git rebase upstream/develop
```
- 리베이스를 수행함으로써, 커밋 그래프를 깔끔하게 유지할 수 있다.
- git-flow 전략을 위해 활용

## 체리 픽 cherry-pick
```bash
git cherry-pick {특정 커밋의 해시값}
```
- 현재 브랜치에 원하는 커밋만 가져올 수 있다.

#### 참고 자료
- https://backlog.com/git-tutorial/kr/stepup/stepup7_4.html
