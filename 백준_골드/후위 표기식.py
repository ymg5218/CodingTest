# 1918
def solution():
    result = ""
    stack = []

    for s in logic:
        if s == "(":
            stack.append(s)
        elif s == ")":
            while stack[-1] != "(":
                result += stack.pop()
            stack.pop()
        elif s == "+" or s == "-":
            while stack and stack[-1] != "(":
                    result += stack.pop()
            stack.append(s)
        elif s == "*" or s == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    result += stack.pop()
            stack.append(s)
        else:
            result += s
    if stack:
        while stack:
            result += stack.pop()

    return result
if __name__ == "__main__":
    logic = list(input())

    result = solution()

    print(result)