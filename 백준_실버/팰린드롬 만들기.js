// 1213

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim();

function solution() {
    const arr = input.split('').sort();

    var now_idx = 0;
    // 현재 어떤 문자를 확보했고, 다음 문자와 같은지 확인하고싶은 상태
    var isComparing = false;
    var center = "";

    var stack_1 = [];
    var stack_2 = [];

    while (now_idx < arr.length) {
        // 현재 비교하려는 문자가 없는 상태에서 그 다음 문자를 탐색
        // 일단 stack_1에 담아둠
        if (!isComparing) {
            stack_1.push(arr[now_idx]);
            isComparing = true;
        }
        // 현재 비교하려는 문자가 있는 상태에서 그 다음 문자를 탐색
        else {
            // stack_1에 마지막으로 push 된 문자와 같은지 비교. 같으면 그 둘이 한 쌍이 되면 됨.
            if (stack_1[stack_1.length - 1] === arr[now_idx]) {
                stack_2.push(arr[now_idx]);
                // 비교가 끝났으니 false로 다시 바꿔줌.
                isComparing = false;
            }
            else {
                // 하나 쯤은 짝을 이루지 못해도 됨. 팰린드롬 정 가운데에 위치하면 되니까.
                if (center === "") {
                    // 정 가운데에 위치하게 해야하니 일단 stack_1에서 pop 시킴.
                    center = stack_1.pop();
                    // 현재 탐색하는 문자를 stack_1에 push 하고 해당 문자를 기준으로 비교를 시작
                    stack_1.push(arr[now_idx]);
                }
                // 이미 짝을 못 이루는 문자가 존재하는데 또 그런 문자가 존재하면 절대 팰린드롬이 될 수 없음.
                else {
                    return "I'm Sorry Hansoo"
                }
            }

        }

        now_idx += 1;
    }

    // 탐색을 다 완료하였는데, 짝이 없어 팰린드롬 가운데로 와야 하는 문자가 존재할 수 있음.
    if (center !== "") {
        // 그런데 마지막으로 탐색 중인 문자의 짝을 찾지 못했을 경우는 팰린드롬이 될 수 없음
        if (isComparing) {
            return "I'm Sorry Hansoo";
        }
        // 아니라면 팰린드롬 가운데에 위치하도록 함.
        else {
            stack_1.push(center);
        }
    }



    // stack_2를 pop하며 stack_1에 push함.
    // 해당 로직이 끝나고 stack_1에 존재하는 문자를 차례로 출력하면 해당 문자열이 팰린드롬임.
    while (stack_2.length > 0) {
        stack_1.push(stack_2.pop());
    }

    return stack_1.join('');
}

console.log(solution());