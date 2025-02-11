const http = require("node:http");
const { readFile, readFileSync, writeFileSync} = require("fs");
const { parse } = require("url");

readFile("./strona.html", function (err, html) {
  if (err) {
    throw err;
  }
});

http
  .createServer(function (request, response) {
    const reqUrl = parse(request.url).pathname;
    console.log(reqUrl);

    if(request.method === "POST" && reqUrl === "/add") {
        let body = ''
        request.on('data', function(data) {
            body += data
        })
        request.on('end', function() {

            let data = JSON.parse(body);

            let file = readFileSync('./dane.json');
            let currentData = JSON.parse(file.toString());

            let lastId = currentData.students[currentData.students.length-1].id;

            let newUser = {
                ...data,
                id:lastId+1,
            }
            currentData.students.push(newUser);


            writeFileSync('./dane.json',JSON.stringify(currentData));





            response.writeHead(200, {'Content-Type': 'text/html'})
            response.end('meow')
        })
    }


    if (reqUrl == "/add") {
      readFile("./formularz.html", function (err, html) {
        response.write(html);
        response.end();
      });

      return;
    }

    readFile(`./${reqUrl}`, function (err, data) {
      if (err) {
        readFile("./strona.html", function (err, html) {
          response.write(html);
          response.end();
        });
      }

      if (data) {
        response.write(data);
        response.end();
      }
    });
  })
  .listen(8000);
