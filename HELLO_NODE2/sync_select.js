var MySql = require('sync-mysql');
 
var connection = new MySql({
	host		: "localhost", // 데이터베이스 주소
	port		: "3305", // 데이터베이스 포트
	user		: "root", // 로그인 계정
	password	: "python", // 비밀번호
	database	: "python", // 엑세스할 데이터베이스
});
 
const result = connection.query('SELECT * from emp');
console.log(result);
