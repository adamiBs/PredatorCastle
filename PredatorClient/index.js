const express = require('express');
var path = require("path");
const app = express();
const PORT = 3000;

app.use('/static', express.static('public'))

app.get('/', function (req, res) {

    res.sendFile(path.join(__dirname + '/views/index.html'));
    //res.send('Hello World!');

});

app.listen(PORT, function () {
    console.log('Example app listening on port 3000!')
})
