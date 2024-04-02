const mysql  = require('mysql');
const connection = mysql.createConnection({
  host: "localhost", // 데이터베이스 주소
  port: "3305", // 데이터베이스 포트
  user: "root", // 로그인 계정
  password: "python", // 비밀번호
  database: "emp", // 엑세스할 데이터베이스
});

connection.connect();

connection.query('SELECT * from emp', (error, rows, fields) => {
  if (error) throw error;
  console.log('User info is: ', rows);
});

connection.end();