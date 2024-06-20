// 1924

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(file).toString();

const [m, d] = input.split(" ");
const is_31th = [1, 3, 5, 7, 8, 10, 12];
const is_30th = [4, 6, 9, 11];
const dayOfTheWeek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"];

// 0 1 2 3 4 5 6
// 월 화 수 목 금 토 일
let now = 0;

let now_month = 1;
let now_day = 1;

while (1) {
    if (now_month == m) {
        while (d > now_day) {
            now = ((now + 1) % 7);
            now_day = now_day + 1;
        }

        break
    }
    if (is_31th.includes(now_month)) {
        now = ((now + 3) % 7);
    }
    else if (is_30th.includes(now_month)) {
        now = ((now + 2) % 7);
    }
    now_month = now_month + 1;
}

console.log(dayOfTheWeek[now]);
