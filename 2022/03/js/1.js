const fs = require("fs");
let data = fs.readFileSync("i.txt").toString().split(/\r?\n/);
let n = 0

console.log(n);

console.log(data.reduce((a1, e) => a1 + e.substring(0, e.length / 2).split("").reduce((a2, c) => {
    if (a2 != 0 || e.substring(e.length / 2).indexOf(c) == -1) return a2;
    if (c.charCodeAt(0) < 97) return c.charCodeAt(0) - 65 + 27;
    return c.charCodeAt(0) - 96;
}, 0), 0));