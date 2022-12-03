const fs = require("fs");
let data = fs.readFileSync("i.txt").toString();
console.log(data.split(/\r?\n/)
    .map(e => [e.charCodeAt(0), e.charCodeAt(2)])
    .map(([a, b]) => (b - 81 - ((a - b + 27) % 3) * 3))
    .reduce((acc, n) => acc + n));
