const mysql  = require('mysql');
const connection = mysql.createConnection({
  host		: "localhost", // 데이터베이스 주소
  port		: "3305", // 데이터베이스 포트
  user		: "root", // 로그인 계정
  password	: "python", // 비밀번호
  database	: "python" // 엑세스할 데이터베이스
});

connection.connect();
var sql='INSERT INTO emp (e_id,e_name,gen,addr) VALUES(?,?,?,?)';
var param=[1,'1','1','1'];

connection.query(sql,param, (error, result) => {
	 console.log(result.affectedRows)
});

connection.end();