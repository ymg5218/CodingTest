# 1213

def solution():
    stack_1 = []
    stack_2 = []

    now_idx = 0
    center = ""

    isValid = False
    while now_idx < length:
        if not isValid:
            stack_1.append(name[now_idx])
            isValid = True
        else:
            if stack_1[-1] != name[now_idx]:
                if center == "":
                    center = stack_1.pop()
                    stack_1.append(name[now_idx])
                else:
                    return "I'm Sorry Hansoo"
            else:
                stack_2.append(name[now_idx])
                isValid = False

        now_idx += 1
    
    if center != "":
        if isValid:
            return "I'm Sorry Hansoo"
        else: 
            stack_1.append(center)
    
    while stack_2:
        stack_1.append(stack_2.pop())
    
    return "".join(stack_1)


if __name__ == "__main__":
    name = list(input())
    name.sort()

    length = len(name)

    print(solution())