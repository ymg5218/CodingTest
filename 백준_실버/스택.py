# 10828

def push(x):
    global size
    stack.append(x)
    size += 1

def empty():
    global size
    if size == 0:
        return 1
    else:
        return 0

def top():
    global size
    if size == 0:
        return -1
    else:
        size -= 1
        return stack[-1]
    

if __name__ == "__main__":
    n = int(input())
    stack = []
    size = 0

    for _ in range(n):
        op = input()
        if op == "pop":
            if size == 0:
                print(-1)
            else:
                print(stack.pop())
                size -= 1
        elif op == "size":
            print(size)
        elif op == "empty":
            print(empty())
        elif op == "top":
            print(top())
        else:
            _op,_x = op.split()
            x = int(_x)
            push(x)