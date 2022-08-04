const http = require('http');

const host = 'localhost';
const port = 8000;

let listener = function (req, res) {
    res.writeHead(200);
    res.end("Hello World");
}

const server = http.createServer(listener);

server.listen(port, host, () => {
    console.log(`Server running ${host}:${port}`);
});
