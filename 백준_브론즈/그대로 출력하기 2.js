const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().split("\n");

input.forEach(function (result) {
    console.log(result);
})