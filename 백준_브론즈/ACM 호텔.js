// 10250

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(file).toString().split("\n");

const T = parseInt(input[0]);

for (let i = 1; i <= T; i++) {
    // 호텔의 층 수
    nowArr = input[i].trim().split(" ");

    let N = parseInt(nowArr[0]);
    let W = nowArr[1];
    let M = nowArr[2];

    let roomOrder = Math.ceil(M / N);
    let floorOrder = Math.ceil(M % N) * 100;
    if (floorOrder == 0) {
        floorOrder = N * 100;
    }

    console.log(floorOrder + roomOrder);
}; 