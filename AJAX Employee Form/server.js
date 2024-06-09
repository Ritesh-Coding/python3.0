var express = require('express');
var mysql = require('mysql')

var app = express();

var bodyParser = require("body-parser")

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "JOB_APP_DB_29"
  });


  app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));
// use res.render to load up an ejs view file
let PORT = 8092;

app.use(bodyParser.urlencoded({ extended: true }))
app.get('/',function(req,res){
    let data= [{}]
    res.render('form.ejs',{data})
})

app.post('/save',function(req,res){

    console.log(req.body)

})
app.listen(PORT)
console.log("server is listening at port ",PORT)