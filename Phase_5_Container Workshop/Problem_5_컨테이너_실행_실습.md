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

```
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
```
ersatzvitamin9579@c4r3s1 codyssey2026 % docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    e2ac70e7319a   13 days ago   10.1kB
ubuntu        latest    f794f40ddfff   5 weeks ago   78.1MB
ersatzvitamin9579@c4r3s1 codyssey2026 % 

```
docker ps-a로 추적해보면 다음과 같은 화면이 나온다.
```
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
```
ersatzvitamin9579@c4r3s1 codyssey2026 % docker run -it --name my-container -p 8000:80 ubuntu /bin/bash
root@8bd4f3fc96b5:/# 
```
바로 실행된 컨테이너의 root에 들어올 수 있었다!

바로 기본 터미널 명령어를 실행해 보자.
ls, cd, mkdir, rm, rmdir 등을 실행해 보았다.

```
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

들어간 컨테이너에서 나오려면 `Ctrl + d` 명령어를 사용할 수 있다. 

#### attach

root 상태에서는 내가 attach되어 있다.
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
