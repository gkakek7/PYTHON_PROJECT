const express = require('express')
const ejs = require("ejs");
const app = express()
const port = 3000
const bodyParser = require("body-parser");
const database = require("./database");

app.set("view engine", "ejs");
app.use(express.static(__dirname + '/'));
app.use(bodyParser.json());


app.get('/api/emp_selects', async (req, res) => {
    const result = await database.run("SELECT * FROM emp");
	console.log("/api/emp_selects",result);
    res.send(result)
});


app.post('/api/emp_select', async (req, res) => {
	var e_id = req.body.e_id;
	console.log("e_id",e_id);
	var sql =`
		SELECT * FROM emp
		where
		e_id ='${e_id}'
	`;
	console.log("sql",sql);
    const result = await database.run(sql);
	console.log("/api/emp_select",result);
    res.send(result)
});

app.post('/api/emp_insert', async (req, res) => {
	var e_name = req.body.e_name;
	var sex = req.body.sex;
	var addr = req.body.addr;
	
	var sql =`
		insert into emp
			(e_name,sex,addr)
		values
			('${e_name}','${sex}','${addr}')
	`;
    await database.run(sql);
    const result = await database.run("SELECT * FROM emp");
	console.log("/api/emp_select",result);
    res.send(result);
});


app.post('/api/emp_update', async (req, res) => {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var sex = req.body.sex;
	var addr = req.body.addr;
	
	var sql =`
		update emp
		set
			e_name = '${e_name}', 
			sex = '${sex}', 
			addr = '${addr}'
		where
			e_id = '${e_id}'
		
	`;
    await database.run(sql);
    const result = await database.run("SELECT * FROM emp");
	console.log("/api/emp_select",result);
    res.send(result);
});

app.post('/api/emp_delete', async (req, res) => {
	var e_id = req.body.e_id;

	var sql =`
		delete from emp
		where
			e_id = '${e_id}'
		
	`;
    await database.run(sql);
    const result = await database.run("SELECT * FROM emp");
	console.log("/api/emp_delete",result);
    res.send(result);
});




app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});