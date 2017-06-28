const express = require('express');
const father = require('./scripts/father');
const app = express();
const PORT = 2424;

app.post('/api/data', father.handleRequest);

//app.use(function (req, res) {
//    res.send(404);
//});

app.listen(PORT, function () {
    console.log('Example app listening on port ' + PORT + '!')
})
