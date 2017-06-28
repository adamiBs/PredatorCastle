const express = require('express')
const app = express()
const PORT = 3000

app.get('/', function(req,res){
       
     //res.sendFile('index.html');
    res.send('Hello World!');

});

app.listen(PORT, function () {
  console.log('Example app listening on port 3000!')
})