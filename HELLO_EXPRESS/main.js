const express = require('express');
const app = express();
const port = 3000;
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));
app.set("view engine", "ejs");
app.set('views', './views');
app.use('/static',express.static('static'));

app.get('/', (req, res) => {
	res.send('Hello World!')
})

app.get('/param', (req, res) => {
	var menu = req.query.menu
	res.send('PARAM:'+ menu)
})

app.post('/post', (req, res) => {
	var menu=req.body.menu;
	console.log(menu)
	res.send('PARAM:'+menu)
})

app.get('/forw', (req, res) => {
	var a = "홍길동";
	var b = ["전우치","홍길동"];
	var c = [
		{e_id:'1',e_name:'1',addr:'1',gen:'1'},
		{e_id:'2',e_name:'2',addr:'2',gen:'2'},
		{e_id:'3',e_name:'3',addr:'3',gen:'3'}
	]
	res.render("forw",{a:a,b:b,c:c})
})

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`)
})