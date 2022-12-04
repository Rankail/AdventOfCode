const fs = require("fs");
let data = fs.readFileSync("i.txt").toString().split(/\r?\n/);
console.log(data.reduce((acc, l) => {
    [a, b, c, d] = l.split(/,|-/).map(c => parseInt(c, 10));
    if ((a <= c && b >= d) || (c <= a && d >= b)) return acc + 1;
    return acc;
}, 0));