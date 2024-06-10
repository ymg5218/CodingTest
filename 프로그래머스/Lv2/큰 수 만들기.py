def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1

        stack.append(number[i])

    while k > 0:
        stack.pop()
        k -= 1

    return "".join(stack)

if __name__ == "__main__":
    number = "4177252841"
    k = 4

    print(solution(number, k))