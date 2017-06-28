const express = require('express'); 
var cors = require('cors')
var bodyParser = require('body-parser')
const father = require('./scripts/father');
const app = express();
const PORT = 2424;

app.use(cors());
app.use(bodyParser.json())

app.post('/api/data', father.handleRequest);

app.use(function (req, res) {
    res.send(404);
});

app.listen(PORT, function () {
    console.log('Example app listening on port ' + PORT + '!')
})
