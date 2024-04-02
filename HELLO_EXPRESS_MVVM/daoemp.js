var mysql = require('sync-mysql');

class DaoEmp {
	constructor() {
		this.conn = new mysql({
			host: 'localhost',
			port: 3305,
			user: 'root',
			password: 'python',
			database: 'python'
		});
	}
	selectList() {
		var list = this.conn.query('SELECT * FROM emp');
		return list
	}
	select(e_id) {
		var list = this.conn.query(`SELECT * FROM emp WHERE e_id='${e_id}'`);
		return list[0];
	}
	insert(e_id,e_name,gen,addr) {
		var result = this.conn.query(`INSERT INTO emp (e_id,e_name,gen,addr) VALUES ('${e_id}','${e_name}','${gen}','${addr}')`)
		return result.affectedRows;
	}
	update(e_name,gen,addr,e_id) {
		var result = this.conn.query(`UPDATE emp SET e_name='${e_name}', gen='${gen}',addr='${addr}' WHERE e_id='${e_id}'`)
		return result.affectedRows;
	}
	delete(e_id) {
		var result = this.conn.query(`DELETE FROM emp WHERE e_id='${e_id}'`)
		return result.affectedRows;
	}
}
module.exports = DaoEmp;