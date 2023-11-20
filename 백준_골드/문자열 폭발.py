# 9935

def solution():
    stack = []
    now = 0
    bomb_len = len(bomb)
    str_len = len(str)

    while(now < str_len):
        stack.append(str[now])
        compair_str = ''.join(stack[-bomb_len : ])
        if compair_str == bomb:
            for _ in range(bomb_len):
                stack.pop()

        now += 1

    if stack:
        result = ''.join(stack)
        print(result)
    else:
        print("FRULA")


if __name__ == "__main__":
    str = input()
    bomb = input()
    solution()