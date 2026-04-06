# Problem 7: 포트 매핑 접속 증거

## 포트 매핑(Port mapping)이란?
한 마디로 호스트 포트 <-> 컨테이너 포트를 연결하는 것을 말한다.

컨테이너를 포트 매핑하는 형태: `docker run -p 3000:80 my-app`: 
    ㄴ> docker run (컨테이너 run 할게) | -p 3000:80 (포트 맵핑-호스트3000:컨테이너80)| 이름은 my-app이다

말인즉슨, 호스트 포트에서 localhost:3000으로 접속할 때, 돌아가는 컨테이너 내부의 포트 80 에서 실행 중인 앱에서 접속할 수 있다는 말이다.



## 1. 포트 매핑 설정

### 기본 설정법
가장 간단하게는 상술한
> docker run -p [호스트 포트]:[도커 포트] [포트 이름]  
으로 포트 매핑을 설정할 수 있다.
간단한 테스트를 할 때 사용 가능하다.

### Dockerfile에서 적어두기
이를 Dockerfile에서 설정하려면:
```dockerfile
FROM ngnix

EXPOSE 80
```
과 같이 어떤 포트를 사용하는지 **문서화**까지는 가능하지만, 실제 매핑은 자동으로 되지 않으므로 실행할 때 -p 옵션을 함께 써야 한다. 이미지를 build할 때 주로 사용한다.

### docker-compose.yml에서 설정하기

```yaml
version: '3'
services:
    web:
        image:my-app
        ports:
            - 8000:80

```
과 같이 작성해둘 수 있는 듯하다. 복잡한 프로젝트를 만들 때 사용한다.


## 2. 포트 매핑 접속 증거 (curl 응답)

우선 nginx 이미지를 활용해 web-nginx 서버를 localhost:8888 에서 돌아가게 해 보자.

`docker run --name web-nginx -p 8888:80 nginx`에서 -p 8888:80 부분이 port mapping이다.
```
ersatzvitamin9579@c4r3s1 codyssey2026 % docker run --name web-nginx -p 8888:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
ec781dee3f47: Already exists 
bb3d0aa29654: Already exists 
510ddf6557d6: Already exists 
cde7a05ae428: Already exists 
587e3d84dbb5: Already exists 
3189680c601f: Already exists 
5e815e07e569: Already exists 
Digest: sha256:7150b3a39203cb5bee612ff4a9d18774f8c7caf6399d6e8985e97e28eb751c18
Status: Downloaded newer image for nginx:latest
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/04/06 13:44:39 [notice] 1#1: using the "epoll" event method
2026/04/06 13:44:39 [notice] 1#1: nginx/1.29.7
2026/04/06 13:44:39 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2026/04/06 13:44:39 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
2026/04/06 13:44:39 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
2026/04/06 13:44:39 [notice] 1#1: start worker processes
2026/04/06 13:44:39 [notice] 1#1: start worker process 29
2026/04/06 13:44:39 [notice] 1#1: start worker process 30
2026/04/06 13:44:39 [notice] 1#1: start worker process 31
2026/04/06 13:44:39 [notice] 1#1: start worker process 32
2026/04/06 13:44:39 [notice] 1#1: start worker process 33
2026/04/06 13:44:39 [notice] 1#1: start worker process 34
192.168.215.1 - - [06/Apr/2026:13:45:11 +0000] "GET / HTTP/1.1" 200 896 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15" "-"
192.168.215.1 - - [06/Apr/2026:13:45:11 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8888/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15" "-"
2026/04/06 13:45:11 [error] 30#30: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.215.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8888", referrer: "http://localhost:8888/"
```

다음과 같이 스크린샷으로 확인할 수 있다.

![포트매핑](/codyssey2026/Problem1_AI_SW_Setup/Phase_7_Port_Mapping/nginx_screenshot.png)


바로 curl을 써서 내용을 확인해 보자.(로그 확인)

```
ersatzvitamin9579@c4r3s1 codyssey2026 % docker ps
CONTAINER ID   IMAGE                 COMMAND                   CREATED          STATUS          PORTS                                     NAMES
343478e145ae   nginx                 "/docker-entrypoint.…"   2 minutes ago    Up 4 seconds    0.0.0.0:8888->80/tcp, [::]:8888->80/tcp   web-nginx # -> 작동 중!
518e3b4a0dcf   my-custom-nginx:1.0   "/docker-entrypoint.…"   30 minutes ago   Up 30 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   my-web
87923d3a78e5   busybox               "sh"                      5 hours ago      Up 2 hours                                                relaxed_chebyshev
8bd4f3fc96b5   ubuntu                "/bin/bash"               5 hours ago      Up 5 hours      0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   my-container
ersatzvitamin9579@c4r3s1 codyssey2026 % 

ersatzvitamin9579@c4r3s1 codyssey2026 % curl localhost:8888
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, nginx is successfully installed and working.
Further configuration is required for the web server, reverse proxy, 
API gateway, load balancer, content cache, or other features.</p>

<p>For online documentation and support please refer to
<a href="https://nginx.org/">nginx.org</a>.<br/>
To engage with the community please visit
<a href="https://community.nginx.org/">community.nginx.org</a>.<br/>
For enterprise grade support, professional services, additional 
security features and capabilities please refer to
<a href="https://f5.com/nginx">f5.com/nginx</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
ersatzvitamin9579@c4r3s1 codyssey2026 % 

```

