const express = require('express');
const app = express();
const PORT = 2424;

app.post('/', function (req, res) {
    //res.json({"hello": "world"});
      res.send('Hello World!')
});

//app.use(function (req, res) {
//    res.send(404);
//});

app.listen(PORT, function () {
    console.log('Example app listening on port ' + PORT + '!')
})
