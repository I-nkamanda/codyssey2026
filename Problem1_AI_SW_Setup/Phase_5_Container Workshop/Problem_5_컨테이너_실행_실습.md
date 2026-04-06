# Problem 5: 컨테이너 실행 실습

이제 다운로드 받은 latest ubuntu 이미지를 가지고 컨테이너를 실행시켜 보자.
기본 형태는
> docker run [modifier] --name [container이름] [사용할 이미지] [실행할 명령어] 형태이다.
>> -it (interactive하게 -tty(터미널)을 쓰겠다)
>> --name ()  괄호 속의 이름을 쓰겠다
>> 사용할 이미지

`docker run -it --name my-container ubuntu /bin/bash` 의 경우는
"ubuntu 이미지로 my-container라는 컨테이너를 interactive terminal을 사용해서 만들 거고, /bin/bash/ 실행해줘" 라고 해석할 수 있는 것이다.


## 1. 테스트: hello-world 실행해보기!
hello-world 이미지를 실행해 보자. 이 이미지는 Docker 환경 점검용 기본 테스트 용도로 쓴다.

`docker run hello-world`로 실행해볼 수 있다. hello-world 이미지를 pull 해올 수도 있지만, local에 없으면 자동으로 pull해서 온다. 

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
Digest: sha256:452a468a4bf985040037cb6d5392410206e47db9bf5b7278d281f94d1c2d0931
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```
### 이렇게 Docker 설치 + 데몬 + 컨테이너 실행 환경이 정상임을 확인 가능하다.


`docker images` 명령어를 사용해 보면 깨알같이 hello-world 이미지가 추가되어 있음을 확인할 수 있다!!
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    e2ac70e7319a   13 days ago   10.1kB
ubuntu        latest    f794f40ddfff   5 weeks ago   78.1MB
ersatzvitamin9579@c4r3s1 codyssey2026 % 

```
hello-world라는 컨테이너가 실제로 돌아갔는지 docker ps-a로 추적해보면 다음과 같은 화면이 나온다.
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps -a
CONTAINER ID   IMAGE         COMMAND       CREATED          STATUS                      PORTS                                     NAMES
989e07f2cba1   hello-world   "/hello"      40 seconds ago   Exited (0) 40 seconds ago                                             focused_bassi
2fdd80f128c2   hello-world   "/hello"      4 minutes ago    Exited (0) 4 minutes ago                                              modest_wing
8bd4f3fc96b5   ubuntu        "/bin/bash"   28 minutes ago   Up 7 minutes                0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container
ff061a1140ac   ubuntu        "/bin/bash"   55 minutes ago   Exited (0) 55 minutes ago                                             trusting_leakey
b8474ec34dee   ubuntu        "my-image"    56 minutes ago   Created                                                               flamboyant_cohen
ersatzvitamin9579@c4r3s1 codyssey2026 % 

```
역시 실행하자마자 바로 종료됨을 확인할 수 있다!

## 2. 직접 ubuntu 컨테이너 실행을 해본 뒤, 내부 진입 후 명령 실행해 보기

윗 단계에서 받아놓은 ubuntu 이미지를 활용, my-container라는 컨테이너를 만들어 보겠다.

`docker run -it --name my-container -p 8000:80 ubuntu /bin/bash` 를 입력해 보자.
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker run -it --name my-container -p 8000:80 ubuntu /bin/bash
root@8bd4f3fc96b5:/# 
```
바로 실행된 컨테이너의 root에 들어올 수 있었다!

바로 기본 터미널 명령어를 실행해 보자.
ls, cd, mkdir, rm, rmdir 등을 실행해 보았다.

```bash
root@8bd4f3fc96b5:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@8bd4f3fc96b5:/# cd bin

root@8bd4f3fc96b5:/bin# cd ..
root@8bd4f3fc96b5:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@8bd4f3fc96b5:/# cd usr
root@8bd4f3fc96b5:/usr# ls
bin  games  include  lib  lib64  libexec  local  sbin  share  src
root@8bd4f3fc96b5:/usr# mkdir alex
root@8bd4f3fc96b5:/usr# ls
alex  bin  games  include  lib  lib64  libexec  local  sbin  share  src
root@8bd4f3fc96b5:/usr# rm alex
rm: cannot remove 'alex': Is a directory
root@8bd4f3fc96b5:/usr# rmdir alex
root@8bd4f3fc96b5:/usr# ls
bin  games  include  lib  lib64  libexec  local  sbin  share  src
```



## 3. 컨테이너 종료/유지의 차이를 관찰 및 정리하기

#### 컨테이너 종료해 보기

>`docker stop [컨테이너명]` 을 사용하면 컨테이너를 종료할 수 잇다.


#### 컨테이너에서 그냥 나오기

들어간 컨테이너에서 나오려면 `Ctrl + d` 명령어를 사용할 수 있다. 또는 내부에서 `>exit` 명령어를 사용해도 된다.

#### attach
>`docker attach [컨태이너명]`이라는 명령어를 사용한다.
- 이 명령어 사용 시, 컨테이너의 기존 프로세스(PID1)에 바로 연결한다.
- 기존 프로세스의 출력/입력도 같이 공유를 한다.

`docker run`을 실행하면 자동으로 새 컨테이너 생성 + 실행을 하게 된다.
이 때, -it option이 들어간 상황이라면 컨테이너가 실행되자마자 터미널 세션에 연결(attach) 된다.
예를 들어서 `docker run -it --name my-container ubuntu:latest /bin/bash`입력 시
- 컨테이너 안의 /bin/bash shell로 들어가서 명령어를 입력 가능하고
- Ctrl + d 나 `exit`으로 나왔을 때 컨테이너는 종료가 된다 (PID 1이 /bin/bash이기 때문에)


my-container가 돌아가는 상황에서 실행을 해 보자.

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker attach my-container
root@8bd4f3fc96b5:/# ls
root@8bd4f3fc96b5:/usr# exit #exit 이후에
exit
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps #내가 연 컨테이너가 종료 되어있음을 확인할 수 있다
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps -a #ps-a 를 활용해서 확인 시
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                        PORTS     NAMES
8bd4f3fc96b5   ubuntu    "/bin/bash"   6 minutes ago    Exited (127) 15 seconds ago             my-container # 이와 같이 15초 전에 종료되었다고 뜬다!
ff061a1140ac   ubuntu    "/bin/bash"   32 minutes ago   Exited (0) 32 minutes ago               trusting_leakey
b8474ec34dee   ubuntu    "my-image"    34 minutes ago   Created                                 flamboyant_cohen
```


```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker start my-container
my-container
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                      PORTS                                     NAMES
8bd4f3fc96b5   ubuntu    "/bin/bash"   6 minutes ago    Up 6 seconds                0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container
ff061a1140ac   ubuntu    "/bin/bash"   33 minutes ago   Exited (0) 33 minutes ago                                             trusting_leakey
b8474ec34dee   ubuntu    "my-image"    34 minutes ago   Created                                                               flamboyant_cohen
ersatzvitamin9579@c4r3s1 codyssey2026 % 


```

#### exec

`docker exec`명령어는 **이미 실행 중인 컨테이너** 안에서 명령어를 실행하는 명령이다. 
- 이미 실행 중인 컨테이너 안에서 새로은 프로세스/shell을 실행하는 것이다.
- PID1 이 아닌 독립된 PID를 가지고 새 프로세스가 생성되기 때문에 기존 프로세스에 영향 없음.
- 인터랙티브 shell (`docker exec -it my-container /bin/bash`)도 실행 가능하다.


그러므로, `docker run`처럼 새 컨테이너를 만드는 것이 아니라 살아있는 컨테이너에 들어가거나 명령을 실행할 떄 쓴다.
사용법:
> docker exec [옵션] <컨테이너 이름|ID> <명령어>
- <컨테이너 이름|ID> 는 `docker ps`로 확인할 수 있다.
- <명령어>는 익히 아는 /bin/bash 등을 사용할 수도 있고 이외에도 여러가지 있다.
- [옵션] 의 경우는 `-i`(표준 입력-stdin 유지), `-t` (터미널 할당) 등 여러가지가 있다.

예시로 `docker exec -it my-container /bin/bash`를 실행해 보자.
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps       
CONTAINER ID   IMAGE     COMMAND       CREATED       STATUS             PORTS                                     NAMES
8bd4f3fc96b5   ubuntu    "/bin/bash"   2 hours ago   Up About an hour   0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container
ersatzvitamin9579@c4r3s1 codyssey2026 % docker exec -it my-container /bin/bash
root@8bd4f3fc96b5:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@8bd4f3fc96b5:/# cd usr
root@8bd4f3fc96b5:/usr# ls
bin  games  include  lib  lib64  libexec  local  sbin  share  src
root@8bd4f3fc96b5:/usr# cd bin
root@8bd4f3fc96b5:/usr/bin# exit
exit

```
이 상태에서 `docker ps`를 실행해 보면

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED       STATUS             PORTS                                     NAMES
8bd4f3fc96b5   ubuntu    "/bin/bash"   2 hours ago   Up About an hour   0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container

```
다음과 같이, my-container는 여전히 잘 돌아가고 있음을 확인해 볼 수 있다!!

## 4. 기타
#### PID1?

- 컨테이너가 실행되고 가장 먼저 실행된 프로세스의 Process ID는 1일 것이다.
- 그러므로 Docker 관점에서는 컨테이너의 사실상 "메인 프로세스" 역할을 한다.(실행해야 하니까)
- 그래서, PID1 = OS 전체의 init 프로세스처럼 특별한 기능도 일부 있다고 한다.
> 그래서 docker run 명령어 라인 끝부분에 얹은 명령어가 PID1이 되며, 컨테이너 종료 결정권을 가지고 있다. 
> 그러므로 PID1이 종료되면 컨테이너 전체가 종료된다. (Ctrl+D) 등으로 shell을 종료할 시에도 그렇다.



#### busybox?
hello-world 같이 메시지만 출력하고 뿅 사라지는 이미지 말고도 busybox 라는 명령어 실행이 가능한 image가 있다고 해서 또 테스트해보았다!

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker run -it busybox
Unable to find image 'busybox:latest' locally
latest: Pulling from library/busybox
481282afbc43: Pull complete 
Digest: sha256:1487d0af5f52b4ba31c7e465126ee2123fe3f2305d638e7827681e7cf6c83d5e
Status: Downloaded newer image for busybox:latest
/ # ls
bin    dev    etc    home   lib    lib64  proc   root   sys    tmp    usr    var
/ # 
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS                                     NAMES
8bd4f3fc96b5   ubuntu    "/bin/bash"   35 minutes ago   Up 14 minutes   0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container
```
역시 나오니까 바로 컨테이너가 종료된다. 옵션을 
`docker run -it busybox tail -f /dev/null`와 같이 넣어주면 지속적으로 실행된다고 한다.

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps -a
CONTAINER ID   IMAGE         COMMAND       CREATED              STATUS                          PORTS                                     NAMES
87923d3a78e5   busybox       "sh"          About a minute ago   Exited (0) About a minute ago                                             relaxed_chebyshev
989e07f2cba1   hello-world   "/hello"      8 minutes ago        Exited (0) 8 minutes ago                                                  focused_bassi
2fdd80f128c2   hello-world   "/hello"      12 minutes ago       Exited (0) 12 minutes ago                                                 modest_wing
8bd4f3fc96b5   ubuntu        "/bin/bash"   36 minutes ago       Up 15 minutes                   0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container
ff061a1140ac   ubuntu        "/bin/bash"   About an hour ago    Exited (0) About an hour ago                                              trusting_leakey
b8474ec34dee   ubuntu        "my-image"    About an hour ago    Created                                                                   flamboyant_cohen
ersatzvitamin9579@c4r3s1 codyssey2026 % 

```

이것을 어떻게 활용해볼 수 있을까?

`docker run -it busybox`를 써서 Docker 설치 확인 및 명령어 테스트를 해볼 수도 있을 것이고, 컨테이너 생성/삭제 및 파일 조작 연습도 가능하다. 

또한, `docker run busybox echo "Hello from BusyBox"` 와 같은 명령어를 입력해 보면 컨테이너 실행 -> 명령 실행 -> 바로 종료 같은 느낌으로, CI/CD 파이프라인에서 간단한 명령어를 테스트해볼 수도 있다고 한다.
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker run busybox echo "Hello from BusyBox"
Hello from BusyBox # 실행이 된다!
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps -a
CONTAINER ID   IMAGE         COMMAND                   CREATED             STATUS                         PORTS                                     NAMES
9a63d3437ef2   busybox       "echo 'Hello from Bu…"   5 seconds ago       Exited (0) 6 seconds ago                                                 nifty_montalcini
87923d3a78e5   busybox       "sh"                      About an hour ago   Exited (0) About an hour ago                                             relaxed_chebyshev
989e07f2cba1   hello-world   "/hello"                  About an hour ago   Exited (0) About an hour ago                                             focused_bassi
2fdd80f128c2   hello-world   "/hello"                  About an hour ago   Exited (0) About an hour ago                                             modest_wing
8bd4f3fc96b5   ubuntu        "/bin/bash"               2 hours ago         Up About an hour               0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container
ff061a1140ac   ubuntu        "/bin/bash"               2 hours ago         Exited (0) 2 hours ago                                                   trusting_leakey
b8474ec34dee   ubuntu        "my-image"                2 hours ago         Created                                                                  flamboyant_cohen
ersatzvitamin9579@c4r3s1 codyssey2026 % 

```
