# 5972
import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(start_v):
    queue = deque()

    INF = 50000 * 1000 + 1
    costs = [INF for _ in range(N + 1)]

    queue.append(start_v)
    costs[1] = 0

    while queue:
        now_v = queue.popleft()
        next = graph[now_v][:]
        while next:
            next_v, cost = next.pop()
            if costs[now_v] + cost < costs[next_v]:
                costs[next_v] = costs[now_v] + cost
                queue.append(next_v)

    return costs[N]



if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        v1, v2, c = map(int, input().split())
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])
    
    print(dijkstra(1))