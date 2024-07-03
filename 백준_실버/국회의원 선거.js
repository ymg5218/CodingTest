// 1417

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split("\n").map(Number);

const N = input.shift();
let myVotes = input.shift();

function solution() {
    if (N === 1) {
        return 0;
    }

    let max = Math.max(...input);
    let count = 0

    while (myVotes <= max) {
        input[input.indexOf(max)] -= 1;
        myVotes += 1;
        count += 1;
        max = Math.max(...input);
    }
    return count;
}

console.log(solution())