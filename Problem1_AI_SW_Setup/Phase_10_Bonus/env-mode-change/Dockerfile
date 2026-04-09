# Dockerfile
FROM node:18-alpine 
# 베이스 이미지를 가져오고

WORKDIR /usr/src/app
#컨테이너 안에 /usr/src/app을 만들어 주고

COPY package*.json ./
#내 컴퓨터(호스트)의 package.json, package-lock.json 파일을
#컨테이너 안의 /usr/src/app 폴더로 복사

RUN npm install
# /usr/src/app 폴더에서 npm install 실행 

COPY . .

# 컨테이너가 시작될 때 이 명령어를 실행합니다.
CMD [ "node", "app.js" ]