// 10815

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const haveCards = input[1].split(" ").map((i) => parseInt(i)).sort((a, b) => a - b);
let checkCards = input[3].split(" ").map((i) => parseInt(i));
const N = parseInt(input[0]);
const M = parseInt(input[2]);

function binarySearch(target) {
    let left = 0;
    let right = N - 1;

    let mid = Math.floor((left + right) / 2);

    while (left <= right) {
        if (target === haveCards[mid]) {
            return true;
        }
        else if (target > haveCards[mid]) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
        mid = Math.floor((left + right) / 2);
    }

    return false;
}

for (let i = 0; i < M; i++) {
    if (binarySearch(checkCards[i])) {
        checkCards[i] = 1;
    }
    else {
        checkCards[i] = 0;
    }
}

console.log(checkCards.join(" "));

