def binary_bit(num):
    # 31(11111)같은 모든 자리수가 1인 경우 대비, 한 자리수 더 크게 사이즈 잡기
    result = [0]
    length = 1
    stack = []
    while num > 0:
        stack.append(num % 2)
        num //= 2
        length += 1
    
    while stack:
        result.append(stack.pop())

    return result, length

def solution(numbers):
    answer = []

    for idx in range(len(numbers)):
        now = numbers[idx]
        
        # 현재 수가 짝수 -> 2^0 자리수를 0에서 1로 치환
        if now % 2 == 0:
            answer.append(now + 1)
        # 현재 수가 홀수 -> 가장 자리수가 작은 0을 1로 치환, 해당 자리수 기준 오른쪽 1을 0으로 치환
        else:
            now_binary, now_length = binary_bit(now)
            for idx in range(now_length - 1, -1, -1):
                if now_binary[idx] == 0:
                    now_binary[idx] = 1
                    now_binary[idx + 1] = 0
                    break
            next = 0
            for i in range(now_length):
                next += (now_binary[i] * 2**(now_length - i - 1))
            answer.append(next)
        

    return answer

if __name__ == "__main__":
    numbers = [2, 7]
    print(solution(numbers))