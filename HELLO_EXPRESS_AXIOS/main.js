const express = require('express');
const app = express();
const port = 3000;
const axios = require('axios');
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));
app.set("view engine", "ejs");
app.set('views', './views');
app.use(express.static('static'));

app.get('/', (req, res) => {
	res.send('Hello World!')
})
app.post('/ajax', (req, res) => {
	let menu=req.body.menu;      // 사용자의 JSON 요청
    res.send({result:'success(ajax)'});
})
app.post('/fetch', (req, res) => {
	//let menu=req.body.menu;      // 사용자의 JSON 요청
    res.send({result:'success(fetch)'});
})
app.post('/axios', (req, res) => {
	let menu=req.body.menu;      // 사용자의 JSON 요청
    res.send({result:'success(fetch)'});
})
app.listen(port, () => {
	console.log(`Example app listening on port ${port}`)
})