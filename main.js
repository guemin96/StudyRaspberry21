//javascript Node.js 
// 웹서버 작동시키는 것이기 때문에 꼭 필요!!!!!
var http = require('http');
http.createServer(function(req,res){
    res.writeHead(200,{'Content-Type': 'text/plain'});
    res.end('Hello Node.Js\n');
}).listen(8080,'127.0.0.1');
console.log('Server is running at http://127.0.0.1:8080');