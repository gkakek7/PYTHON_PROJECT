var MySql = require('sync-mysql');
 
var connection = new MySql({
	host		: "localhost", // 데이터베이스 주소
	port		: 3305, // 데이터베이스 포트
	user		: "root", // 로그인 계정
	password	: "python", // 비밀번호
	database	: "python", // 엑세스할 데이터베이스
});
var e_id= '6';
var e_name= '4';
var gen= '4';
var addr= '4';
var sql=`delete from emp where e_id=${e_id}`
console.log(sql)
const result = connection.query(sql);
console.log(result.affectedRows);
