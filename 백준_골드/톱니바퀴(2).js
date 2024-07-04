// 15662

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split("\n");

// 데이터 스플릿
const T = parseInt(input[0].trim());

// 인덱스 편하게 접근하기 위해 0번 인덱스는 더미
var gear = [[-1]];
// N극은 0, S극은 1
// 12시 방향부터 시계방향대로 극이 주어짐
for (let i = 1; i <= T; i++) {
    gear.push(input[i].trim().split('').map(Number));
}

const K = parseInt(input[T + 1]);

var lotate = [];
for (let i = T + 2; i < input.length; i++) {
    lotate.push(input[i].trim().split(' ').map(Number));
}

// 기어가 시계 혹은 반시계로 계속 회전하게되니 큐 자료구조를 활용
/**
 * 회전한 기어의 2번 인덱스 < -- > 오른쪽 기어의 6번 인덱스 
 * 회전한 기어의 6번 인덱스 < -- > 왼쪽 기어의 2번 인덱스
 */
for (let idx = 0; idx < K; idx++) {
    const [now_gear, lotat_direct] = lotate[idx];

    var gears_lotate = Array.from({ length: T + 1 }, () => 0);
    gears_lotate[now_gear] = lotat_direct;

    let left_gear = -1;
    let right_gear = -1;

    if (now_gear === 1) {
        right_gear = now_gear + 1;
    }
    else if (now_gear === T) {
        left_gear = now_gear - 1;
    }
    else {
        left_gear = now_gear - 1;
        right_gear = now_gear + 1;
    }

    // 회전 기어의 왼쪽 기어들 차례로 확인
    let now_lotat_direct = lotat_direct * -1; // 현재 회전 방향
    if (left_gear !== -1) {
        for (let left = left_gear; left > 0; left--) {
            // 왼쪽 기어 A와 A의 오른쪽 기어인 B 기어의 맞닿는 극이 다르면 왼쪽 기어 회전
            if (gear[left][2] != gear[left + 1][6]) {
                gears_lotate[left] = now_lotat_direct;
                now_lotat_direct *= -1;
            }
            // 회전 영향을 안받는다면 종료
            else {
                break;
            }
        }
    }
    // 회전 기어의 오른쪽 기어들 차례로 확인
    now_lotat_direct = lotat_direct * -1;
    if (right_gear !== -1) {
        for (let right = right_gear; right <= T; right++) {
            // 왼쪽 기어 A와 A의 오른쪽 기어인 B 기어의 맞닿는 극이 다르면 오른쪽 기어는 회전
            if (gear[right - 1][2] != gear[right][6]) {
                gears_lotate[right] = now_lotat_direct;
                now_lotat_direct *= -1;
            }
            // 회전 영향을 안받는다면 종료
            else {
                break;
            }
        }
    }

    // 모든 기어 일제히 회전시킴.
    for (let g = 1; g <= T; g++) {
        if (gears_lotate[g] === 0) continue;
        // 시계방향으로 돌아야 함.
        else if (gears_lotate[g] === 1) {
            temp = gear[g].pop();
            gear[g].unshift(temp);
        }
        // 반시계방향으로 돌아야 함.
        else {
            temp = gear[g].shift();
            gear[g].push(temp);
        }
    }
}

let cnt = 0;

for (let i = 1; i <= T; i++) {
    if (gear[i][0] === 1) {
        cnt += 1;
    }
}
console.log(cnt)
