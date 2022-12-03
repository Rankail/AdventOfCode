const fs = require("fs");
let data = fs.readFileSync("i.txt").toString();
let p = data.split(/\r?\n\r?\n/)
let r = p.map(r => r.split(/\r?\n/).reduce((acc, n) => acc + parseInt(n, 10), 0)).reduce((acc, n) => Math.max(acc, n), 0);
console.log(r)