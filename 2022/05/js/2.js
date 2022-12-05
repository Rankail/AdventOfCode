const data = require("fs").readFileSync("i.txt").toString().split(/\r?\n\r?\n/).map(e => e.split(/\r?\n/));
let stackInput = data[0];
let moveInput = data[1];

const c = (stackInput[0].length + 1) / 4;
let stacks = Array(c).fill("");
for (let s of stackInput.slice(0, c - 1).reverse()) {
    for (let i = 0; i < c; i++) {
        if (s[i * 4 + 1] != " ") {
            stacks[i] += s[i * 4 + 1];
        }
    }
}
for (let l of moveInput) {
    m = l.match(/move (\d*) from (\d*) to (\d*)/);
    stacks[parseInt(m[3]) - 1] += stacks[parseInt(m[2]) - 1].slice(-parseInt(m[1]));
    stacks[parseInt(m[2]) - 1] = stacks[parseInt(m[2]) - 1].slice(0, -parseInt(m[1]));
}
console.log(stacks.reduce((acc, s) => acc + s.at(-1), ""));