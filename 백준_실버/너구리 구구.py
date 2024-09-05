# 18126
from collections import deque

def bfs():
    queue = deque()
    # 현재 탐색한 정점과 해당 정점까지의 거리
    queue.append([1, 0])
    visited[1] = True

    while queue:
        now_v, now_dis = queue.popleft()
        for next_v, next_dis in tree[now_v]:
            if not visited[next_v]:
                distance[next_v] = now_dis + next_dis
                visited[next_v] = True
                queue.append([next_v, distance[next_v]])

    return max(distance)



if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        v1, v2, d = map(int, input().split())
        tree[v1].append([v2, d])
        tree[v2].append([v1, d])

    distance = [0 for _ in range(N + 1)]
    visited = [False] * (N + 1)

    print(bfs())