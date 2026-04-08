# 첫 번째 꼭지: 타이핑 에러 또는 argument의 실수


타이핑 에러를 통해서 보이는 수많은 에러들

관찰:

주로 명령어에서 `docker images`를 `docker image`와 같이,  `docker logs`를 `docker log`로, `docker stats`를 `docker stat`와 같이 타이핑하고는 낭패를 보는 경우가 많은 듯 했다.

그래 놓고 Git은  `git log` `git status` 같이 비슷한데 다른 명령어들이 들어가 있으니 혼돈이 컸었다.

가설: 명령어 숙지가 부족해서 발생한 문제이다. 또는 argument를 잘못 입력한 것이다. 

해결 방법: argument를 정확히 입력하고, 명령어를 정확히 입력한다. 




# 두 번째 꼭지: 끝아지 않은 따옴표와 dquote> 의 지옥

나는 분명
`% echo "HERE'S LOOKING AT YOU, AGAIN!" > bind-test/host-test.txt`
라는 명령어를 입력했는데, 쉘은 
```bash
dquote>
```
를 기어이 띄우고 마는 것이었다.
그래서 
```bash
dquote> '
dquote> "
```
이렇게 따옴표를 닫아줄 때까지 계속 나를 물고 놓아주지 않다가 따옴표가 닫히고 나자마자
```bash 
HERE'S LOOKING AT YOU, AGAIN > bind-test/host-test.txt
'
```
echo 이하 구절을 모두 string으로 복명복창하고 끝나는 것이었다.

깨달음: "HERE'S LOOKING AT YOU, AGAIN"안의 HERE'S 부분을 자세히 보자.
이 E와 S 사이의 `'`가 쉘에게는 '여기서부터 따옴표 시작이야' 또는 '여기서부터 따옴표 끝이야'라고 인식되는 것이었다. 

해결: "HERE\'S LOOKING AT YOU, AGAIN!" 으로 역이스케이프를 해주었다. 



# 세 번째 꼭지: 여러 컴퓨터에서 작업하다 git pull을 누르자마자 몰아친 .DS_Store의 악몽

교육장 아이맥으로 작업을 하다가 repository에 올려주고, 또 개인 맥북으로 작업을 하다가 push하는 것을 반복했다. 그러다가 그만...

교육장 iMac에서 git pull 을 하기 전에 VSCode에서 파일들을 보다 보니 .DS_Store 파일(맥 파일 시스템에서 폴더를 열 때마다 자동으로 생성하는 metadata 파일)이 변경되어서 그런지 git pull을 하자마자...

```bash
rsatzvitamin9579@c4r3s1 codyssey2026 % git pull
remote: Enumerating objects: 53, done.
remote: Counting objects: 100% (53/53), done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 43 (delta 13), reused 42 (delta 12), pack-reused 0 (from 0)
오브젝트 묶음 푸는 중: 100% (43/43), 996.50 KiB | 23.73 MiB/s, 완료.
https://github.com/I-nkamanda/codyssey2026 URL에서
   703c6b1..81b6576  main       -> origin/main
업데이트 중 703c6b1..81b6576
error: 다음 파일의 로컬 변경 사항을 병합 때문에 덮어 쓰게 됩니다:
	.DS_Store
병합하기 전에 변경 사항을 커밋하거나 스태시하십시오.
중지함
```
git pull이 중단되었다니!

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % git status
현재 브랜치 main
브랜치가 'origin/main'보다 2개 커밋 뒤에 있고, 앞으로 돌릴 수 있습니다.
  (로컬 브랜치를 업데이트하려면 "git pull"을 사용하십시오)

커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (use "git restore <file>..." to discard changes in working directory)
	수정함:        .DS_Store

```

그래서 `git rm --cached .DS__Store`명령어를 입력해서 .DS_Store 를 추적하는 것을 멈춰주고 .gitignore 파일을 만등러서 GitHub에 올리지 않을 파일 목록을 급조했다.

그 뒤에 다시 git commit을 하고 다시 git pull을 하자마자...

```bash
rsatzvitamin9579@c4r3s1 codyssey2026 % git pull
remote: Enumerating objects: 53, done.
remote: Counting objects: 100% (53/53), done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 43 (delta 13), reused 42 (delta 12), pack-reused 0 (from 0)
오브젝트 묶음 푸는 중: 100% (43/43), 996.50 KiB | 23.73 MiB/s, 완료.
https://github.com/I-nkamanda/codyssey2026 URL에서
   703c6b1..81b6576  main       -> origin/main
업데이트 중 703c6b1..81b6576
error: 다음 파일의 로컬 변경 사항을 병합 때문에 덮어 쓰게 됩니다:
	.DS_Store
병합하기 전에 변경 사항을 커밋하거나 스태시하십시오.
중지함
ersatzvitamin9579@c4r3s1 codyssey2026 % git status
현재 브랜치 main
브랜치가 'origin/main'보다 2개 커밋 뒤에 있고, 앞으로 돌릴 수 있습니다.
  (로컬 브랜치를 업데이트하려면 "git pull"을 사용하십시오)

커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (use "git restore <file>..." to discard changes in working directory)
	수정함:        .DS_Store

```

또 다시 충돌이 일어났다.
그래서 GPT와 제미나이의 도움을 받아서 `git pull --no-rebase`명령어를 입력하자...
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % git pull --no-rebase
CONFLICT (modify/delete): .DS_Store deleted in HEAD and modified in 81b65763328d729a3b1270827faf48fe99f38ed6.  Version 81b65763328d729a3b1270827faf48fe99f38ed6 of .DS_Store left in tree.
자동 병합이 실패했습니다. 충돌을 바로잡고 결과물을 커밋하십시오.

```
`git status`를 입력하니 나오는 내용은...
```bash
병합하지 않은 경로:
  (해결했다고 표시하려면 알맞게 "git add/rm <파일>..."을 사용하십시오)
	이 쪽에서 삭제: .DS_Store
```
결국 `git rm .DS_Store`를 사용한 뒤에 다시 커밋을 하니까
```
ersatzvitamin9579@c4r3s1 codyssey2026 % git rm .DS_Store
rm '.DS_Store'
ersatzvitamin9579@c4r3s1 codyssey2026 % git commit -m "Merge remote-tracking branch 'origin/main' and keep .DS_Store deleted"
[main 5efe1b8] Merge remote-tracking branch 'origin/main' and keep .DS_Store deleted

```
와 같이 .DS_Store 를 완전히 삭제하고 나서야 git pull --no-rebase 에서 나온 충돌이 끝났고, 파일들이 업데이트되었다.


원인: 내가 .DS_Store의 존재를 몰랐엇고, .gitignore도 만들지 않았어서 생긴 문제엿다.

해결 방안: 앞으로는 프로젝트 폴더 만들 때 .DS_Store도.. .
.gitignore에 먼저 넣고 진행해야 할 것이다. (프로젝트 시작 시 루틴화하기)