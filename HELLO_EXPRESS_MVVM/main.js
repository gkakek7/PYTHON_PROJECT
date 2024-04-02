const express = require('express');
const app = express();
const port = 3000;

// DAO import
var DaoEmp = require('./daoemp');
var de = new DaoEmp();
// bodyParser 설정
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : false }));
// ejs 설정
app.set('view engine', 'ejs');
app.set('views', './views');
app.use(express.static('static'));
// axios 설정
var axios = require('axios');


app.post('/emp_list', function(req, res) {
	var emps = de.selectList();
	res.json({emps:emps});
});

app.post('/emp_mod', function(req, res) {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	var cnt = de.update(e_id,e_name,gen,addr);
	res.json({cnt:cnt});
});

app.post('/emp_del', function(req, res) {
	var e_id = req.body.e_id;
	var cnt = de.delete(e_id);
	res.json({cnt:cnt});
});

app.post('/emp_add', function(req, res) {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	var cnt = de.insert(e_id,e_name,gen,addr);
	res.json({cnt:cnt});
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});