// 2578

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split("\n");

function isBingo(board) {
    let bingo = 0;
    if (board[0][0] === board[1][1] && board[1][1] === board[2][2] && board[2][2] === board[3][3] && board[3][3] === board[4][4]) {
        bingo += 1;
    }

    if (board[4][0] === board[3][1] && board[3][1] === board[2][2] && board[2][2] === board[1][3] && board[1][3] === board[0][4]) {
        bingo += 1;
    }

    for (let row = 0; row < 5; row++) {
        if (board[row][0] === board[row][1] && board[row][1] === board[row][2] && board[row][2] === board[row][3] && board[row][3] === board[row][4]) {
            bingo += 1;

            if (bingo >= 3) {
                return true;
            }
        }
    }

    for (let col = 0; col < 5; col++) {
        if (board[0][col] === board[1][col] && board[1][col] === board[2][col] && board[2][col] === board[3][col] && board[3][col] === board[4][col]) {
            bingo += 1;

            if (bingo >= 3) {
                return true;
            }
        }
    }

    return false;
}

var board = [];
// 각 숫자가 위치해있는 좌표 정보
var coordinate = {};

let seq = 0;
for (let i = 0; i < 5; i++) {
    _row = input[i].trim().split(" ");
    board.push(_row);
    for (let n = 0; n < 5; n++) {
        coordinate[_row[n]] = seq;
        seq += 1;
    }
}

result = 1
for (let i = 5; i < 10; i++) {
    var row = input[i].trim().split(" ");
    for (let idx = 0; idx < 5; idx++) {
        const now_coordinate = coordinate[row[idx]];

        const now_row = Math.floor(now_coordinate / 5);
        const now_col = now_coordinate % 5;

        board[now_row][now_col] = -1;

        if (isBingo(board)) {
            console.log(result);
            process.exit(0);
        }

        result += 1;
    }
}

