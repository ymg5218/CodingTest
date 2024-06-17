# 11724
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    visited[start_v] = True

    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (N + 1)

    result = 0
    for i in range(1, N + 1):
        if not visited[i]:
            result += 1
            bfs(i)

    print(result)
