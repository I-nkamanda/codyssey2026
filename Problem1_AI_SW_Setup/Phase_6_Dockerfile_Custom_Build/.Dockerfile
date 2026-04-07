# 베이스 이미지 지정
FROM ubuntu:latest

# 작성자 정보
LABEL maintainer="ersatzvitamin@gmail.com"

# 환경 설정: 패키지 설치시 "할까요? (y/n)"" 물어보는 것들을 전자동화(noninteractive로 설정)
ENV DEBIAN_FRONTEND=noninteractive

# 작업 디렉토리 설정
WORKDIR /app

# 파일 복사
COPY . /app

# 의존성 설치
RUN npm install && apt-get update && apt-get install -y curl


# 포트 노출
EXPOSE 80

# 실행 명령어
CMD ["bash"]