# Docker 커스텀 이미지 만들기 - Nginx 웹서버 예제

## 📋 프로젝트 구조

```
project/
├── Dockerfile          # Docker 이미지 빌드 설정
├── index.html         # 커스텀 HTML 콘텐츠
├── nginx.conf         # 커스텀 Nginx 설정
├── .dockerignore      # Docker 빌드 제외 파일
└── README.md          # 이 파일
```

---

## 🎯 학습 목표

1. **베이스 이미지 활용**: 공식 Nginx 이미지를 기반으로 커스텀 이미지 생성
2. **정적 콘텐츠 교체**: 기본 HTML을 커스텀 HTML로 변경
3. **설정 파일 교체**: Nginx 설정을 커스텀 설정으로 변경
4. **이미지 빌드 및 실행**: Docker 명령어 실습

---

## 📝 Dockerfile 상세 설명

```dockerfile
FROM nginx:latest
```
- **베이스 이미지**: 공식 Nginx 이미지 사용
- 이미 웹서버가 설치되고 설정된 상태로 시작

```dockerfile
WORKDIR /usr/share/nginx/html
```
- **작업 디렉토리**: 정적 파일이 저장될 경로 설정
- Nginx는 이 디렉토리의 파일을 웹으로 제공

```dockerfile
RUN rm -f /usr/share/nginx/html/index.html
```
- **기본 파일 제거**: Nginx의 기본 index.html 삭제
- 우리의 커스텀 파일로 교체하기 위함

```dockerfile
COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf
```
- **파일 복사**: 호스트의 파일을 컨테이너로 복사
- 커스텀 HTML과 설정을 이미지에 포함

```dockerfile
EXPOSE 80
```
- **포트 노출**: 컨테이너의 80번 포트를 외부에 노출
- 실제로 포트를 열지는 않고, 문서화 역할

```dockerfile
CMD ["nginx", "-g", "daemon off;"]
```
- **기본 명령**: 컨테이너 시작 시 Nginx 실행
- `daemon off;` 옵션으로 포그라운드에서 실행 (컨테이너가 종료되지 않도록)

---

## 🔧 커스텀 Nginx 설정 주요 기능

### 1. Gzip 압축
```nginx
gzip on;
gzip_comp_level 6;
```
- 텍스트 파일 압축으로 전송 속도 향상

### 2. 정적 파일 캐싱
```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 30d;
}
```
- 이미지, CSS, JS 파일을 30일간 캐시
- 클라이언트 성능 향상

### 3. 헬스 체크 엔드포인트
```nginx
location /health {
    return 200 "healthy\n";
}
```
- Docker, Kubernetes 등에서 컨테이너 상태 확인 용도

---

## 🚀 사용 방법

### 1단계: 이미지 빌드

```bash
# 현재 디렉토리의 Dockerfile을 사용하여 이미지 빌드
docker build -t my-nginx:1.0 .

# 빌드 진행 상황 확인
docker build -t my-nginx:1.0 . --progress=plain
```

**빌드 과정 설명:**
- `docker build`: 이미지 빌드 명령
- `-t my-nginx:1.0`: 이미지 이름과 태그 지정
- `.`: 현재 디렉토리의 Dockerfile 사용

### 2단계: 이미지 확인

```bash
# 빌드된 이미지 확인
docker images | grep my-nginx

# 이미지 상세 정보 확인
docker inspect my-nginx:1.0
```

### 3단계: 컨테이너 실행

```bash
# 기본 실행
docker run -p 8080:80 my-nginx:1.0

# 백그라운드 실행 (권장)
docker run -d -p 8080:80 --name my-web-server my-nginx:1.0

# 포트 매핑 + 환경 변수 + 리소스 제한
docker run -d \
  -p 8080:80 \
  --name my-web-server \
  --memory=256m \
  --cpus=0.5 \
  my-nginx:1.0
```

**포트 매핑 설명:**
- `-p 8080:80`: 호스트의 8080 포트 → 컨테이너의 80 포트
- 브라우저에서 `http://localhost:8080` 접속 가능

### 4단계: 컨테이너 확인 및 관리

```bash
# 실행 중인 컨테이너 확인
docker ps

# 컨테이너 로그 확인
docker logs my-web-server
docker logs -f my-web-server  # 실시간 로그

# 컨테이너 접속
docker exec -it my-web-server bash

# 컨테이너 중지
docker stop my-web-server

# 컨테이너 삭제
docker rm my-web-server
```

### 5단계: 웹 접속 확인

```bash
# 브라우저에서 접속
http://localhost:8080

# 또는 curl 명령으로 확인
curl http://localhost:8080
curl http://localhost:8080/health
```

---

## 🔍 실습 과제

### 과제 1: 이미지 빌드 및 실행
```bash
docker build -t my-nginx:1.0 .
docker run -d -p 8080:80 --name web my-nginx:1.0
curl http://localhost:8080
```

### 과제 2: 커스텀 HTML 수정
1. `index.html` 파일 수정
2. 이미지 다시 빌드: `docker build -t my-nginx:1.1 .`
3. 새 컨테이너 실행: `docker run -d -p 8081:80 my-nginx:1.1`
4. 변경 사항 확인

### 과제 3: Nginx 설정 수정
1. `nginx.conf` 파일 수정 (예: 포트 변경, 로그 포맷 변경)
2. 이미지 다시 빌드
3. 변경 사항 확인

### 과제 4: 다중 포트 실행
```bash
docker run -d -p 8080:80 --name web1 my-nginx:1.0
docker run -d -p 8081:80 --name web2 my-nginx:1.0
docker run -d -p 8082:80 --name web3 my-nginx:1.0

# 각각 다른 포트로 접속 가능
curl http://localhost:8080
curl http://localhost:8081
curl http://localhost:8082
```

---

## 📊 이미지 크기 최적화

### 현재 이미지 크기 확인
```bash
docker images my-nginx:1.0
```

### 크기 줄이기 팁

1. **멀티스테이지 빌드** (고급)
```dockerfile
FROM nginx:alpine  # 더 작은 베이스 이미지 사용
```

2. **불필요한 파일 제거**
```dockerfile
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
```

3. **레이어 최소화**
```dockerfile
# 나쁜 예: 여러 RUN 명령
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

# 좋은 예: 하나의 RUN 명령
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

---

## 🐛 트러블슈팅

### 문제 1: 포트가 이미 사용 중
```bash
# 기존 컨테이너 중지
docker stop my-web-server
docker rm my-web-server

# 또는 다른 포트 사용
docker run -d -p 8081:80 my-nginx:1.0
```

### 문제 2: 파일이 복사되지 않음
```bash
# Dockerfile과 같은 디렉토리에 파일이 있는지 확인
ls -la

# .dockerignore에 파일이 제외되지 않았는지 확인
cat .dockerignore
```

### 문제 3: 컨테이너가 바로 종료됨
```bash
# 로그 확인
docker logs my-web-server

# 컨테이너 상태 확인
docker ps -a
```

---

## 💡 핵심 개념 정리

| 개념 | 설명 |
|------|------|
| **베이스 이미지** | 다른 이미지의 기초가 되는 이미지 (FROM) |
| **레이어** | Dockerfile의 각 명령이 만드는 이미지 계층 |
| **COPY vs ADD** | COPY: 파일 복사, ADD: 파일 복사 + 압축 해제 |
| **RUN vs CMD** | RUN: 빌드 시 실행, CMD: 실행 시 실행 |
| **EXPOSE** | 포트 문서화 (실제로 열지는 않음) |
| **포트 매핑** | 호스트 포트 → 컨테이너 포트 연결 |

---

## 📚 추가 학습 자료

- [Docker 공식 문서](https://docs.docker.com/)
- [Nginx 공식 이미지](https://hub.docker.com/_/nginx)
- [Dockerfile 베스트 프랙티스](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

## ✅ 체크리스트

- [ ] Dockerfile 이해
- [ ] 이미지 빌드 성공
- [ ] 컨테이너 실행 성공
- [ ] 웹 페이지 접속 확인
- [ ] 커스텀 HTML 수정 및 재빌드
- [ ] 커스텀 Nginx 설정 확인
- [ ] 여러 컨테이너 동시 실행
- [ ] 로그 확인 및 분석

---

**Happy Learning! 🎉**
