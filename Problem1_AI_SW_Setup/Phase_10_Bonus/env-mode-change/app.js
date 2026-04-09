// app.js
const express = require('express');
const app = express();

// 1. 환경 변수에서 PORT를 읽어오고, 없으면 기본값으로 3000을 사용합니다.
const PORT = process.env.PORT || 3000; // 8000을 읽으면 dev mode, 9000을 읽으면 production mode

// 2. 환경 변수에서 NODE_ENV를 읽어오고, 없으면 'development'를 기본값으로 사용합니다.
const NODE_ENV = process.env.NODE_ENV || 'development';

app.get('/', (req, res) => {
  res.send(`안녕하세요! 이 서버는 현재 '${NODE_ENV}' 모드입니다.`);
});

app.listen(PORT, () => {
  console.log(`서버가 ${PORT}번 포트에서 실행 중입니다...`);
});