# Problem 8: Docker 볼륨 영속성 검증

Docker를 가지고 만든 컨테이너는 여러가지 일을 할 수 있지만, 컨테이너'만' 사용하는 경우에는
1. image에 미리 들어가있는 내용으로만 시작이 되고,
2. 또 Container가 꺼지면 안에 있는 내용들이 다 날아간다.

그럼 독립된 저장소가 없이 컨테이너만 운영을 할 때는 어떤 문제가 발생하는지 바로 테스트를 해 보겠다.

## 1. 컨테이너 데이터의 휘발성
우선 아무것도 연결하지 않은 컨테이너를 만들어보자. ubuntu 이미지로 "no-volume-test"라는 이름의 컨테이너를 만들었다.
```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % docker run -it --name no-volume-test ubuntu
 bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
76fd055477b6: Pull complete 
Digest: sha256:84e77dee7d1bc93fb029a45e3c6cb9d8aa4831ccfcc7103d36e876938d28895b
Status: Downloaded newer image for ubuntu:latest
```
이제 가볍게 test.txt 파일을 만들고, 컨테이너를 종료해보겠다.
```bash
root@6b790d7a1365:/# echo "hello world" > test.txt
root@6b790d7a1365:/# ls
bin   dev  home  media  opt   root  sbin  sys       tmp  var
boot  etc  lib   mnt    proc  run   srv   test.txt  usr
root@6b790d7a1365:/# cat test.txt
hello world
root@6b790d7a1365:/# exit
exit
```
이제 도커 컨테이너를 제거하고, 다시 새로운 컨테이너를 만들어서 test.txt 파일이 있는지 확인해보자.
```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % docker rm no-volume-test
no-volume-test
jingeollee@Jingeolui-MacBookPro codyssey2026 % docker run -it ubuntu bash
root@4ba914dbb7c3:/# cat test.txt
cat: test.txt: No such file or directory
```
공들여 만들어놓은 test.txt 파일이 없음을 확인할 수 있다.

```bash
root@4ba914dbb7c3:/# ls
bin   dev  home  media  opt   root  sbin  sys  usr
boot  etc  lib   mnt    proc  run   srv   tmp  var

```
ls를 해봐도 없는 것을 확인할 수있다. 결론은? 
#### 컨테이너와 함께 데이터도 날아간다. 즉, 컨테이너는 **휘발성** 이라는 것이다.


그래서 컨테이너 외부의 데이터를 컨테이너 내부로 가져오거나, 컨테이너 내부의 데이터를 컨테이너 외부로 가져오기 위해 volume을 사용하게 된다. 


## 2. Docker 볼륨 생성 및 확인

### 2-1. Volume이란?
하드디스크 저장소 볼륨, 이동식 디스크 저장소 볼륨, 플래쉬 매모리 등. 
가상 저장공간(용량: 容量)을 다루기에 Volume이라고 표현을 한다.

그러면 Docker volume을 생성한 뒤에 컨테이너를 연결한다는 의미란:

컨테이너가 돌아가는 컴퓨터 환경에서 컨테이너가 사용할 수 있는 저장공간(vault)을 일부 미리 만들어 두고, 컨테이너가 액세스할 수 있게 한다는 말이다. 

그렇게 되면 컨테이너를 삭제한다고 해도 데이터 volume은 따로 존재하기 때문에 데이터를 보존할 수 있다.

이제 docker volume을 만들어보자.
```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % docker volume create my-volume
my-volume
```

### 2-2. Docker 볼륨 사용 컨테이너 연결

이렇게 my-volume 을 생성한 뒤에 컨테이너를 연결해보자. -v my-volume:/data 는 my-volume을 /data에 연결한다는 의미이다.
```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % docker run -it --name volume-test -v my-volume:/data ubuntu bash
root@efc8f04b7f10:/# echo "I will persist, even the container that contains me might perish...!" > /data/test.txt
```
test.txt를 만든뒤에 ls를 보면 기본 폴더 이외에 data 폴더가 생긴 것을 확인할 수 있다.
여기서 -v argument 뒤에는 [volume 이름]:[컨테이너 내 volume의 path]이 붙음을 알 수 있다.
```bash
root@efc8f04b7f10:/# cat test.txt
cat: test.txt: No such file or directory
root@efc8f04b7f10:/# ls
bin   data  etc   lib    mnt  proc  run   srv  tmp  var
boot  dev   home  media  opt  root  sbin  sys  usr
root@efc8f04b7f10:/# cat /data/test.txt                                                  
I will persist, even the container that contains me might perish...!
root@efc8f04b7f10:/# exit
exit
```
### 2-3. 컨테이너 삭제를 통한 볼륨 데이터 영속성 검증
이어서 컨테이너를 삭제하고 새 컨테이너에서 동일 볼륨을 연결해 보자.

```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % docker rm volume-test
volume-test. # 삭제를 했다
jingeollee@Jingeolui-MacBookPro codyssey2026 % docker run -it -v my-volume:/data ubuntu bash #이제 이름없는 컨테이너에 my-volume을 연결해서 열어본 뒤에
root@66e12b2ab592:/# cat data/test.txt #/data/test.txt를 찾아보면
I will persist, even the container that contains me might perish...!
```
다음과 같이 데이터는 컨테이너 삭제에 무관하게 volume 내에 안전하게 보관됨을 알 수 있다.

Docker 내부를 보면 (이 layer가 층층히 쌓인 시스템에서) 컨테이너 파일 시스템은 layer 기반으로 (임시로) 만들어진 것이고, 컨테이너는 자기 내부의 /data에 쓰고 있다고 생각하고 있지만, 실제 저장 위치는 컨테이너와는 별도 영역에 존재하는 Docker volume인 것이다. 



## 3. 바인드 마운트 (Bind Mount)

Bind Mount란? 호스트(로컬 환경)의 특정 폴더를 컨테이너 내부의 특정 폴더에 연결하는 것을 말한다. 정확히는 컨테이너가 호스트의 폴더를 '연결'해서 쓰는 것이다.

#### volume과의 차이는?
Volume의 경우는
> [Docker 내부 저장소] -> 컨테이너
로ㅡ Docker가 관리하는 파일 저장소라면, 

Bind Mount는
> [호스트 내부의 내가 지정한 폴더] -> 컨테이너
로, 내가 지정한 폴더를 그대로 컨테이너가 참조하는 것이다.

### 3-1. Bind Mount를 위한 테스트 폴더 만들기

우선 bind-mount를 위한 폴더 "bind-test"를 만들고, 그 안에 test할 파일을 만들어 보자. mount가 된 컨테이너에서는 'Kilroy was here'라는 문구가 출력되도록 할 것이다.

```bash
jingeollee@Jingeolui-MacBookPro Phase_8_Docker_Volume_Continuity % mkdir bind-test
jingeollee@Jingeolui-MacBookPro Phase_8_Docker_Volume_Continuity % echo "Kilroy was here" 
> bind-test/test.txt
jingeollee@Jingeolui-MacBookPro Phase_8_Docker_Volume_Continuity % cat bind-test/test.txt
Kilroy was here
```

### 3-2. Bind-mount로 컨테이너 실행
이제 bind-mount로 컨테이너를 실행해보자. -v ./bind-test:/data 는 ./bind-test를 /data에 bind-mount 한다는 의미이다.
```bash
jingeollee@Jingeolui-MacBookPro Phase_8_Docker_Volume_Continuity % docker run -it -v $(pwd)/bind-test:/data ubuntu bash
root@779482a06e1f:/# ls
bin   data  etc   lib    mnt  proc  run   srv  tmp  var
boot  dev   home  media  opt  root  sbin  sys  usr
root@779482a06e1f:/# cat /data/test.txt
Kilroy was here
root@779482a06e1f:/# 
```
data/test.txt 폴더가 있음을 확인할 수 있었다.
또한, cat 명령어를 입력하자마자 Mac 환경에서 
> "Orbstck.app이 데스크탑 폴더의 파일에 접근하려고 합니다"
라는 시스템 메시지가 뜬 것으로 봐서 bind-mount된 호스트의 폴더를 컨테이너가 읽어들인 것을 터미널 외적으로도 확인할 수 있었다.

### 3-3. Bind-mount 컨테이너 -> 외부 연결 테스트

계속해서 컨테이너 내부에서 파일을 수정한 뒤에 실제 폴더에 반영이 되는지도 테스트해 보겠다. (양방향 테스트)
```bash
root@779482a06e1f:/# echo "SO WAS RED" >> data/test.txt
root@779482a06e1f:/# exit
exit
```
이제 test.txt에는 "SO WAS RED"라는 메시지가 추가되었을 것이다.

```bash
jingeollee@Jingeolui-MacBookPro Phase_8_Docker_Volume_Continuity % cat bind-test/test.txt 
Kilroy was here
SO WAS RED

```
컨테이너->외부폴더 연결이 완료됨을 확인할 수 있었다.

### 3-4. Bind-mount 외부 -> 컨테이너 연결 테스트

이제 반대쪽도 보자. 로컬 바인드 폴더의 내용물을 변경한 뒤에 컨테이너에 반영이 되는지 확인해보자는 이야기다.

우선 bind-test 폴더에 host-test.txt 파일을 만들자.
```bash
jingeollee@Jingeolui-MacBookPro Phase_8_Docker_Volume_Continuity % echo "HERE\'S LOOKING AT YOU, AGAIN" > bind-test/host-test.txt
```
이제 컨테이너를 실행해서 host-test.txt 파일이 있는지 확인해보자. 역시 -v argument를 사용한다. 위치는 $(pwd)/bind-test, 컨테이너 내부는 /data로 연결한다.
```bash
jingeollee@Jingeolui-MacBookPro Phase_8_Docker_Volume_Continuity % docker run -it -v $(pwd)/bind-test:/data ubuntu bash    
root@b360b130423d:/# cat /data/host-test.txt 
HERE\'S LOOKING AT YOU, AGAIN
root@b360b130423d:/# cd data
root@b360b130423d:/data# ls
host-test.txt  test.txt


```
호스트에서 파일을 변경한 것이 컨테이너에도 반영된 것을 확인했다.

그러므로 요약해 보자면...

## 컨테이너 삭제 후 데이터 유실 방지 대안

컨테이너의 writable layer는 기본적으로 휘발성이므로,
삭제 후에도 데이터를 유지하려면 외부 저장소를 연결해야 한다.

대안:
- Docker volume: Docker가 관리하는 영속 저장소를 연결
- Bind mount: 호스트의 특정 폴더를 컨테이너에 연결

실습에서는 volume과 bind mount 둘 다 시험했고,
영속 데이터가 필요할 때는 컨테이너 내부만 믿지 말고 외부 저장소를 연결해야 함을 확인했다.
