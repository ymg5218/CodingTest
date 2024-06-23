// 2920

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().split(" ").map(Number);

let is_ascending = true;
let now = 2;
if (input[0] === 8) {
    is_ascending = false
    now = 7
} else if (input[0] !== 1) {
    console.log("mixed");
    process.exit(0);
}


for (let i = 1; i < 8; i++) {
    if (is_ascending) {
        if (now === input[i]) {
            now++;
        }
        else {
            console.log("mixed");
            process.exit(0)
        }
    }
    else {
        if (now === input[i]) {
            now--;
        }
        else {
            console.log("mixed");
            process.exit(0);
        }
    }
}

if (is_ascending) {
    console.log("ascending");
} else {
    console.log("descending");
}