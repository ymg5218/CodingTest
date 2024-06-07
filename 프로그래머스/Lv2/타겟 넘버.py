# 숫자의 개수는 최대 20개 -> 백트래킹을 통한 완전탐색 경우의 수 : 2^20 -> 시간복잡도 괜찮음

def solution(numbers, target):
    global answer
    global length
    length = len(numbers)
    answer = 0

    back_tracking(numbers, target, [], 0)

    return answer

def back_tracking(numbers, target, ops, seq):
    global answer
    global length
    if seq == length:
        result = 0
        for i in range(seq):
            if ops[i] == "+":
                result += numbers[i]
            else:
                result -= numbers[i]
        if result == target:
            answer += 1
        return
    op = ["+", "-"]
    for i in range(2):
        ops.append(op[i])
        back_tracking(numbers, target, ops, seq + 1)
        ops.pop()

if __name__ == "__main__":
    numbers = [4, 1, 2, 1]
    target = 4

    print(solution(numbers, target))