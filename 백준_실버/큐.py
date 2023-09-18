# 10845

from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque([])
length = 0

for _ in range(N):
    op = sys.stdin.readline().strip()
    if op == "pop":
        if length == 0:
            print(-1)
        else:
            print(queue.popleft())
            length -= 1
    elif op == "size":
        print(length)
    elif op == "empty":
        if length == 0:
            print(1)
        else:
            print(0)
    elif op == "front":
        if length == 0:
            print(-1)
        else:
            print(queue[0])
    elif op == "back":
        if length == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        _op = list(op.split())
        queue.append(_op[1])
        length += 1


