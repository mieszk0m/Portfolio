const express = require("express");
const fs = require("fs");
const bodyParser = require("body-parser"); // For POST data handling

const app = express();
const port = 8001;

// Use middleware for routing, static files, and body parsing
app.use(express.static("public")); // Serve static files from 'public' directory
app.use(bodyParser.json()); // Parse JSON data in POST requests

app.get("/", (req, res) => {
  fs.readFile("./strona.html", (err, data) => {
    res.set("Content-Type", "text/html");

    if (err) {
      res.status(500).send("Error reading strona.html");
      return;
    }
    res.status(200).send(data);
    res.end();
  });
});

app.get("/add", (req, res) => {
  fs.readFile("./formularz.html", (err, data) => {
    if (err) {
      res.status(500).send("Błąd przy czytaniu formularza");
      return;
    }
    res.set("Content-Type", "text/html");

    res.status(200).send(data);
    res.end();
  });
});

app.get("/dane.json", (req, res) => {
    fs.readFile("./dane.json", (err, data) => {
        if (err) {
            res.status(500).send("Błąd przy łatowaniu danych");
            return;
        }
        res.set("Content-Type", "application/json");

        res.status(200).send(data);
        res.end();
    });
});


app.post("/add", async (req, res) => {
  try {
    const fileData = await fs.promises.readFile("./dane.json", "utf8");
    const data = JSON.parse(fileData);
    const lastId = data.students[data.students.length - 1].id;
    const newUser = { id: lastId + 1, ...req.body };
    data.students.push(newUser);
    await fs.promises.writeFile("./dane.json", JSON.stringify(data, null, 2));

    res.status(200).send("meow");
  } catch (error) {
    console.error(error);
    res.status(500).send("Błąd przy dodawaniu studenta");
  }
});

app.listen(port, () => {
  console.log(`Nasłuchiwanie na porcie ${port}`);
});
