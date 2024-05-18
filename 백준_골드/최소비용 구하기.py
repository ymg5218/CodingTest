# 1916
import heapq
import sys

input = sys.stdin.readline


def dijkstra(start_v):
    distance[start_v] = 0

    priority_queue = []

    for next_v in graph[start_v]:
        heapq.heappush(priority_queue, next_v)
        distance[next_v[1]] = min(next_v[0], distance[next_v[1]])

    while priority_queue:
        cost, now_v = heapq.heappop(priority_queue)

        # 가지치기
        if cost > distance[now_v]:
            continue

        for next_v in graph[now_v]:
            if next_v[0] + distance[now_v] < distance[next_v[1]]:
                distance[next_v[1]] = next_v[0] + distance[now_v]
                heapq.heappush(priority_queue, next_v)


if __name__ == "__main__":
    INF = 100000 * 1000 + 1

    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        v1, v2, c = map(int, input().split())
        graph[v1].append([c, v2])

    start, end = map(int, input().split())

    distance = [INF] * (N + 1)

    dijkstra(start)

    print(distance[end])