const express = require('express');
var path = require("path");
const app = express();
const PORT = 3000;

app.use('/static', express.static('public'))

app.get('/', function (req, res) {

    res.sendFile(path.join(__dirname + '/views/index.html'));
    //res.send('Hello World!');

});

app.use(function (req, res) {
    res.send(404);
});

app.listen(PORT, function () {
    console.log('Example app listening on port ' + PORT + '!')
})
