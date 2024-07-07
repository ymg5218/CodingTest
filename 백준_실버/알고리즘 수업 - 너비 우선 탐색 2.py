# 24445
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_v):
    result = [0] * (N + 1)
    queue = deque()
    queue.append(start_v)
    visited[start_v] = True
    seq = 1

    while queue:
        now_v = queue.popleft()
        result[now_v] = seq
        next_v_list = sorted(graph[now_v], reverse=True)

        for next_v in next_v_list:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

        seq += 1

    for i in range(1, N + 1):
        print(result[i])


if __name__ == "__main__":
    N, M, R = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    bfs(R)