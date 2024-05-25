# 13549
from collections import deque


def bfs(start_v):
    queue = deque([])
    queue.append([0, start_v])
    while queue:
        now_time, now_v = queue.popleft()
        if visited[now_v] > now_time or visited[now_v] == -1:
            visited[now_v] = now_time
        else:
            continue

        for next_v in (now_v * 2, now_v - 1, now_v + 1):
            if 0 <= next_v <= 200000:

                if next_v == now_v * 2:
                    queue.append([now_time, next_v])
                else:
                    queue.append([now_time + 1, next_v])

            if visited[K] != -1:
                return visited[K]

if __name__ == "__main__":
    N, K = map(int, input().split())

    visited = [-1 for _ in range(200001)]

    print(bfs(N))