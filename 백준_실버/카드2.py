# 2164

from collections import deque

N = int(input())

queue = deque([])

for idx in range(1, N+1):
    queue.append(idx)

for _ in range(N-1):
    queue.popleft()
    _x = queue.popleft()
    queue.append(_x)

print(queue.popleft())