// 13901

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const [row, col] = input[0].trim().split(' ').map(Number);
const invalid_cnt = parseInt(input[1].trim());
// 갈 수 있는 곳은 0
var board = Array.from(Array(row), () => Array(col).fill(0));

for (let i = 2; i < 2 + invalid_cnt; i++) {
    const invalid = input[i].trim().split(' ').map(Number);
    // 못 가는 곳은 1
    board[invalid[0]][invalid[1]] = 1;
}

var now = input[2 + invalid_cnt].trim().split(' ').map(Number);
board[now[0]][now[1]] = 1;

// 1 : 위, 2 : 아래, 3 : 왼쪽, 4 : 오른쪽
const command = input[input.length - 1].trim().split(' ').map(Number);
let command_idx = 0;
while (true) {
    let canMove = false;
    let straight = true;
    while (command_idx < command.length) {
        const now_row = now[0];
        const now_col = now[1];

        let next_row;
        let next_col;

        if (command[command_idx] === 1) {
            next_row = now_row - 1;
            next_col = now_col;
        }
        else if (command[command_idx] === 2) {
            next_row = now_row + 1;
            next_col = now_col;
        }
        else if (command[command_idx] === 3) {
            next_row = now_row;
            next_col = now_col - 1;
        }
        else {
            next_row = now_row;
            next_col = now_col + 1;
        }

        if (next_row >= 0 && next_row < row && next_col >= 0 && next_col < col && board[next_row][next_col] === 0) {
            canMove = true;
            now = [next_row, next_col];
            board[next_row][next_col] = 1;
        }
        else {
            straight = false
            command_idx += 1;
        }
    }
    // 종료 조건 : 로봇의 상하좌우 어디로도 갈 수 없을 때
    if (!canMove) {
        console.log(now.join(" "));
        break;
    }
    command_idx %= command.length;
}

