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