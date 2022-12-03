const fs = require("fs");
let data = fs.readFileSync("i.txt").toString().split(/\r?\n/);
console.log(data.reduce((a1, d, i) => {
    if (i % 3 !== 0) return a1;
    return a1 + d.split("").filter(c => data[i + 1].indexOf(c) !== -1).reduce((a2, c) => {
        if (a2 !== 0 || data[i + 2].indexOf(c) === -1) return a2;
        if (c.charCodeAt(0) < 97) return c.charCodeAt(0) - 65 + 27;
        return c.charCodeAt(0) - 96;
    }, 0)
}, 0));