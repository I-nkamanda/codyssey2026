# Problem 9: Git 설정 및 GitHub 연동

## git clone

>Git Clone을 사용해서 github에 있는 레포지토리를 내 맥북으로 가져올 수 있다. 
> git clone [리포지토리 url.git] 형태로 사용한다.
```
jingeollee@Jingeolui-MacBookPro sunbal % git clone https://github.com/I-nkamanda/codyssey2026/tree/maihttps://github.com/I-nkamanda/codyssey2026.git
Cloning into 'codyssey2026'...
fatal: repository 'https://github.com/I-nkamanda/codyssey2026/tree/maihttps://github.com/I-nkamanda/codyssey2026.git/' not found
jingeollee@Jingeolui-MacBookPro sunbal % https://github.com/I-nkamanda/codyssey2026.git                  
zsh: no such file or directory: https://github.com/I-nkamanda/codyssey2026.git

```
실패. 명령어를 몇 번씩 잘못 입력했다.
[트러블슈팅](/Problem_xx_트러블슈팅.md)

```
jingeollee@Jingeolui-MacBookPro sunbal % git clone https://github.com/I-nkamanda/codyssey2026.git
Cloning into 'codyssey2026'...
remote: Enumerating objects: 87, done.
remote: Counting objects: 100% (87/87), done.
remote: Compressing objects: 100% (78/78), done.
remote: Total 87 (delta 32), reused 17 (delta 1), pack-reused 0 (from 0)
Receiving objects: 100% (87/87), 30.12 KiB | 10.04 MiB/s, done.
Resolving deltas: 100% (32/32), done.
```


내용을 수정하고 나서 다시 git add . -> commit -> push를 해 보자.
```
jingeollee@Jingeolui-MacBookPro codyssey2026 % git add .
jingeollee@Jingeolui-MacBookPro codyssey2026 % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   .DS_Store
	modified:   "Phase_2_chmod/Problem_2_chmod \354\241\260\354\236\221.md"
	new file:   sth.sh
```
다음과 같이 수정된 파일들이 어떤 것들인지 달려준다.
이제 git commit을 해 보겠다.

```
jingeollee@Jingeolui-MacBookPro codyssey2026 % git commit -m "chmod 항목 추가"
[main 6788aeb] chmod 항목 추가
 Committer: Jingeol Lee <jingeollee@Jingeolui-MacBookPro.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 3 files changed, 113 insertions(+), 1 deletion(-)
 create mode 100755 sth.sh

```
이제 shell에서 push를 해 보자.

```
jingeollee@Jingeolui-MacBookPro codyssey2026 % git push origin main
Username for 'https://github.com': ㅁㅁㅁㅁㅁㅁㅁㅁ
Password for 'https://ㅁㅁㅁㅁㅁㅁㅁ@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/ㅁㅁㅁㅁㅁㅁㅁㅁㅁ/codyssey2026.git/'
```
비밀번호를 적었으나 Shell 상에서는 에러가 나 버렸다.

다시금 PAT(Personal Access Token)을 발급받아서 로그인 시도를 해 보았다.

```
jingeollee@Jingeolui-MacBookPro codyssey2026 % git push origin main
Username for 'https://github.com':  ㅁㅁㅁㅁㅁㅁㅁ@gmail.com
Password for 'https://ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ @github.com': 
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 15 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 2.07 KiB | 2.07 MiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/I-nkamanda/codyssey2026.git
   8ad03c4..6788aeb  main -> main
jingeollee@Jingeolui-MacBookPro codyssey2026 % 

```
다음과 같이 push가 성공한 것을 확인할 수 있다.

VSCode 등의 IDE를 활용,  GitHub 로그인을 미리 해놓았을 경우:

```
ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ@ㅁㅁㅁㅁㅁㅁ codyssey2026 % git commit -m "파일 및 폴더들 구조화 감행함"
[main dc6e723] 파일 및 폴더들 구조화 감행함
 Committer: ㅁㅁㅁ <ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ@ㅁㅁㅁㅁㅁㅁ.ㅁㅁㅁㅁㅁㅁ.kr> #비식별화
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 10 files changed, 0 insertions(+), 0 deletions(-)

 ```

git config --list 결과는 다음과 같다.

```
ersatzvitamin9579@c6r7s1 codyssey2026 % git config --list
credential.helper=osxkeychain
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/I-nkamanda/codyssey2026.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
branch.main.vscode-merge-base=origin/main
```

개인 맥북에서는 다음과 같이 나온다.
```
jingeollee@Jingeolui-MacBookPro codyssey2026 % git config --list
credential.helper=osxkeychain
init.defaultbranch=main
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/I-nkamanda/codyssey2026.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
branch.main.vscode-merge-base=origin/main
jingeollee@Jingeolui-MacBookPro codyssey2026 % 
```
