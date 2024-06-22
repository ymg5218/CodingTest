// 1966

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

const [T, ...testcases] = input;

for (let i = 0; i < T; i++) {
    let M = Number(testcases[2 * i].split(" ")[1]);
    const queue = testcases[2 * i + 1].trim().split(" ").map(Number);
    let target = queue[M];
    let result = 0;

    while (true) {
        const max = Math.max(...queue);
        const number = queue.shift();

        if (number === max) {
            result++;
            if (target === max && M === 0) {
                console.log(result);
                break;
            }
        }
        else {
            queue.push(number);
        }

        if (M === 0) {
            M = queue.length - 1;
        }
        else {
            M--;
        }
    }
}