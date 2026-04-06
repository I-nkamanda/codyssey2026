FROM nginx:latest
## 최신 nginx 이미지를 가져옴. 이미 web 서버가 설치되고 설정된 상태로 시작한다

WORKDIR /usr/share/nginx/html
## 정적 file이 저장될 경로 설정
## Nginx는 이 디렉토리의 파일을 웹으로 제공함


RUN rm -f usr/share/nginx/html/index.html
## 원래 설치되는 정적 index.html을 삭제한다.
## 커스텀 index 파일로 교체하기 위함.

COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf
## 파일 복사하기: HOST의 파일을 컨테이너로 복사한다.
## 커스텀 HTML과 일정을 image에 포함한다.

EXPOSE 80
## 컨테이너의 80번 포트 노출. 실제로 열지는 않고 문서화 역할을 한다.


CMD ["nginx", "-g", "daemon off;"] 
## 컨테이너 시작 시 Nginx 실행 / 옵션으로 컨테이너가 종료되지 않도록 foreground에서 실행됨

