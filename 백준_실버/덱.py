# 10866

import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])
length = 0

for _ in range(N):
    op = sys.stdin.readline().strip()
    if op == "front":
        if length == 0:
            print(-1)
        else:
            print(queue[0])
    elif op == "back":
        if length == 0:
            print(-1)
        else:
            print(queue[-1])
    elif op == "size":
        print(length)
    elif op == "empty":
        if length == 0:
            print(1)
        else:
            print(0)
    else:
        _op = list(map(str,op.split()))
        if _op[0] == "push_front":
            queue.appendleft(_op[1])
            length += 1
        elif _op[0] == "push_back":
            queue.append(_op[1])
            length += 1
        elif _op[0] == "pop_front":
            if length == 0:
                print(-1)
            else:
                print(queue.popleft())
                length -= 1
        else:
            if length == 0:
                print(-1)
            else:
                print(queue.pop())
                length -= 1