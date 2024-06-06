def binary_bit(num):
    result = ""
    length = 0
    stack = []
    while num > 0:
        stack.append(str(num % 2))
        num //= 2
        length += 1
    
    while stack:
        result += stack.pop()

    return result, length

def solution(numbers):
    answer = []

    for idx in range(len(numbers)):
        now = numbers[idx]
        now_binary, now_length = binary_bit(now)
        next = now + 1
        while True:
            diff = 0
            next_binary, next_length = binary_bit(next)

            digit_gap = next_length - now_length

            if digit_gap > 0:
                diff += digit_gap

            for i in range(now_length):
                if now_binary[i] != next_binary[i + digit_gap]:
                    diff += 1
                if diff > 2:
                    next += 1
                    continue
            if diff <= 2:
                answer.append(next)
                break
            next += 1

    return answer

if __name__ == "__main__":
    numbers = [2, 7]
    print(solution(numbers))