function solution(brown, yellow) {
    var answer = [];

    // (가로 + 세로) * 2 + 4 == yellow일 때의 [가로, 세로]가 정답

    // Math.floor(yellow / 2) + 1 까지 확인하는 이유는 yellow가 1일 때도 있기 때문. + 1 을 해주지 않으면 반복문을 수행하지 않음
    for (let i = 0; i < Math.floor(yellow / 2) + 2; i++) {
        if (yellow % i === 0) {
            if ((yellow / i + i) * 2 + 4 === brown) {
                answer.push(yellow / i + 2);
                answer.push(i + 2);
                break;
            }
        }
    }

    return answer;
}

console.log(solution(8, 1))