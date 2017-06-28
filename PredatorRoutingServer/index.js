const express = require('express'); 
var cors = require('cors')
var bodyParser = require('body-parser')
const father = require('./scripts/father');
const app = express();
const PORT = 2424;

//app.use(function (req, res, next) {
//    //    res.header("Access-Control-Allow-Origin", "192.168.1.24");
//    res.header("Access-Control-Allow-Origin", "*");
//    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//    next();
//});

//app.all('/*', function (req, res, next) {
//    res.header("Access-Control-Allow-Origin", "*");
//    res.header("Access-Control-Allow-Headers", "X-Requested-With");
//    next();
//});

app.use(cors());
app.use(bodyParser.json())

app.post('/api/data', father.handleRequest);

app.use(function (req, res) {
    res.send(404);
});

app.listen(PORT, function () {
    console.log('Example app listening on port ' + PORT + '!')
})
