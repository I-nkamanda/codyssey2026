# Problem 4: Docker 기본 운영 명령


## Docker 운영 명령 실행


### [Docker image 확인]

docker images 명령어를 사용해서 이 컴퓨터에 어떤 이미지가 설치되어 있는지- 확인해볼 수 있다.
다만 docker run을 사용했을 때 로컬 컴퓨터에 이미지가 없다면 자동으로 image를 pull해 오기도 한다.
```
ersatzvitamin9579@c4r3s1 codyssey2026 % docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

```
아무것도 깔려있지 않은 것을 볼 수 있다. 이제는 이미지를 다운로드 해 보자.

### [Docker image 다운로드 및 확인]
이때는 docker pull을 쓸 것이다. 그냥 pull만 입력을 하게 된다면...
```
ersatzvitamin9579@c4r3s1 codyssey2026 % docker pull
docker: 'docker pull' requires 1 argument

Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

Run 'docker pull --help' for more information
```
다음과 같이 docker pull [pull할 이미지], 즉 무슨 이미지를 서버에서 당겨올 지 지정해야 하는 것이다.

ubuntu 최신 (latest)이미지를 pull한 뒤에 확인해보겠다.

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker pull ubuntu:latest #ubuntu:latest를 pull하겠다고 입력시에

latest: Pulling from library/ubuntu
817807f3c64e: Pull complete 
Digest: sha256:186072bba1b2f436cbb91ef2567abca677337cfc786c86e107d25b7072feef0c
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
ersatzvitamin9579@c4r3s1 codyssey2026 % docker images #이렇게 확인이 가능하다.
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       latest    f794f40ddfff   5 weeks ago   78.1MB


```



```
여기에 클록
```



### [Docker ps -a]

`docker ps`를 입력하면
> process status. 즉 현재 실행중인 프로세스(프로그램)의 상태 정보를 출력해 준다.

 `docker ps - a`를 입력하면
> all process status. 위의 명령어에 더해서 실행 중료된 프로세스의 상태 까지, 모든 컨테이너들의 상태를 보여준다.
아무것도 깔려있지 않은 상황에서 docker ps 및 ps-a를 입력해 보자.
``` bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps  
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
아무 것도 나오지 않는다.

ubuntu image 를 깐 상태에서 docker run을 돌려보고 docker ps를 입력해 보자.

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker run ubuntu #아무 것도 나오지 않고 종료된다.
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps #여기에도 아무것도 나오지 않지만
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

```
여기서 docker ps -a를 입력해 본다면:

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps -a # -a 를 추가해 보면 만들어지자마자 종료된 container가 하나 있었음을 확인할 수 있다.
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                      PORTS     NAMES
ff061a1140ac   ubuntu    "/bin/bash"   34 seconds ago   Exited (0) 33 seconds ago             trusting_leakey
b8474ec34dee   ubuntu    "my-image"    2 minutes ago    Created                               flamboyant_cohen
ersatzvitamin9579@c4r3s1 codyssey2026 % 


```

### [Docker 로그 확인]
> docker logs [컨테이너 이름]
라는 명령어를 사용한다.

방금 docker ps-a에서 나온 컨테이너 이름을 활용해 보자면:
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker logs flamboyant_cohen
ersatzvitamin9579@c4r3s1 codyssey2026 % docker logs trusting_leakey
ersatzvitamin9579@c4r3s1 codyssey2026 % 

```
아무 것도 나오지 않는다. 왜인가? 컨테이너에서 한 일이 아무것도 없기에, 출력을 할 것이 없는 것이다.

phase 5에서 my-container라는 우분투 기반 컨테이너 실행 및 실스을 한 뒤에 
`docker logs my-container`를 입력해보면...

```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker logs my-container
root@8bd4f3fc96b5:/# #
root@8bd4f3fc96b5:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@8bd4f3fc96b5:/# cd bin
root@8bd4f3fc96b5:/bin# ls
'['                        expr               mountpoint          sleep
 addpart                   factor             mv                  snice
 apt                       faillog            namei               sort
 apt-cache                 fallocate          nawk                split
 apt-cdrom                 false              newgrp              stat
 apt-config                fgrep              nice                stdbuf
 apt-get                   find               nisdomainname       stty
 apt-key                   findmnt            nl                  su
 apt-mark                  flock              nohup               sum
 arch                      fmt                nproc               sync
 awk                       fold               nsenter             tabs
 b2sum                     free               numfmt              tac
 base32                    getconf            od                  tail
 base64                    getent             pager               tar
 basename                  getopt             partx               taskset
 basenc                    gpasswd            passwd              tee
 bash                      gpgv               paste               tempfile
 bashbug                   grep               pathchk             test
 captoinfo                 groups             perl                tic
 cat                       gunzip             perl5.38.2          timeout
 chage                     gzexe              pgrep               tload
 chattr                    gzip               pidof               toe
 chcon                     hardlink           pidwait             top
 chfn                      head               pinky               touch
 chgrp                     hostid             pkill               tput
 chmod                     hostname           pldd                tr
 choom                     i386               pmap                true
 chown                     iconv              pr                  truncate
 chrt                      id                 printenv            tset
 chsh                      infocmp            printf              tsort
 cksum                     infotocap          prlimit             tty
 clear                     install            ps                  tzselect
 clear_console             ionice             ptx                 uclampset
 cmp                       ipcmk              pwd                 umount
 comm                      ipcrm              pwdx                uname
 cp                        ipcs               rbash               uncompress
 csplit                    ischroot           readlink            unexpand
 cut                       join               realpath            uniq
 dash                      kill               rename.ul           unlink
 date                      last               renice              unminimize
 dd                        lastb              reset               unshare
 deb-systemd-helper        lastlog            resizepart          update-alternatives
 deb-systemd-invoke        ld.so              rev                 uptime
 debconf                   ldd                rgrep               users
 debconf-apt-progress      link               rm                  utmpdump
 debconf-communicate       linux32            rmdir               vdir
 debconf-copydb            linux64            run-parts           vmstat
 debconf-escape            ln                 runcon              w
 debconf-set-selections    locale             savelog             wall
 debconf-show              locale-check       script              watch
 delpart                   localedef          scriptlive          wc
 df                        logger             scriptreplay        wdctl
 diff                      login              sdiff               whereis
 diff3                     logname            sed                 which
 dir                       ls                 select-editor       which.debianutils
 dircolors                 lsattr             sensible-browser    who
 dirname                   lsblk              sensible-editor     whoami
 dmesg                     lscpu              sensible-pager      x86_64
 dnsdomainname             lsipc              sensible-terminal   xargs
 domainname                lslocks            seq                 yes
 dpkg                      lslogins           setarch             ypdomainname
 dpkg-deb                  lsmem              setpriv             zcat
 dpkg-divert               lsns               setsid              zcmp
 dpkg-maintscript-helper   man                setterm             zdiff
 dpkg-query                mawk               sg                  zdump
 dpkg-realpath             mcookie            sh                  zegrep
 dpkg-split                md5sum             sha1sum             zfgrep
 dpkg-statoverride         md5sum.textutils   sha224sum           zforce
 dpkg-trigger              mesg               sha256sum           zgrep
 du                        mkdir              sha384sum           zless
 echo                      mkfifo             sha512sum           zmore
 egrep                     mknod              shred               znew
 env                       mktemp             shuf
 expand                    more               skill
 expiry                    mount              slabtop
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
root@8bd4f3fc96b5:/usr# #
root@8bd4f3fc96b5:/usr# hello-world
bash: hello-world: command not found
root@8bd4f3fc96b5:/usr# exit
exit

```



### [Docker 스테이터스 확인]


my-container라는 Docker 컨테이너를 실행한 상태에서 `docker stats`를 입력해 보면 다음과 같다.
```bash
ersatzvitamin9579@c4r3s1 codyssey2026 % docker start my-container
CONTAINER ID   NAME           CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O     PIDS 
8bd4f3fc96b5   my-container   0.00%     1.418MiB / 15.67GiB   0.01%     1.81kB / 642B   1.58MB / 0B   1 
```

이제 터미널에 `docker stop my-container`를 입력, 컨테이너를 멈춘 뒤에 다시 docker stats를 입력해 보면
```bash
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS 

```
비어있음을 확인할 수 있다.

