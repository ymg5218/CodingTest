# 1238
import sys
import heapq

input = sys.stdin.readline

def dijkstra(start_v, distance):
    distance[start_v] = 0
    hq = []
    for next_v in graph[start_v]:
        if next_v[0] + distance[start_v] < distance[next_v[1]]:
            heapq.heappush(hq, next_v)
            distance[next_v[1]] = next_v[0] + distance[start_v]

    while hq:
        time, now_v = heapq.heappop(hq)

        if time > distance[now_v]:
            continue

        for next_v in graph[now_v]:
            if next_v[0] + distance[now_v] < distance[next_v[1]]:
                heapq.heappush(hq, next_v)
                distance[next_v[1]] = next_v[0] + distance[now_v]





if __name__ == "__main__":
    INF = 100 * 100000 + 1
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        start, end, t = map(int, input().split())

        graph[start].append([t, end])

    to_X_distance = [INF] * (N + 1)
    for i in range(1, N + 1):
        distance = [INF] * (N + 1)
        dijkstra(i, distance)
        to_X_distance[i] = distance[X]


    go_home_distance = [INF] * (N + 1)
    dijkstra(X, go_home_distance)

    max_time = 0

    for i in range(1, N + 1):
        total_time = to_X_distance[i] + go_home_distance[i]
        max_time = max(max_time, total_time)

    print(max_time)
