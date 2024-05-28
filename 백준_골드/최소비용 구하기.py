# 1916
import heapq
import sys

input = sys.stdin.readline


def dijkstra(start_v):
    distance[start_v] = 0

    hq = []

    heapq.heappush(hq, [0, start_v])

    while hq:
        now_dis, now_v = heapq.heappop(hq)

        # 가지치기
        if now_dis > distance[now_v]:
            continue

        for next_v in graph[now_v]:
            cost = next_v[0] + distance[now_v]
            if cost < distance[next_v[1]]:
                distance[next_v[1]] = next_v[0] + distance[now_v]
                heapq.heappush(hq, [cost, next_v[1]])


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