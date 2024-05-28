# 1504

import heapq
import sys

input = sys.stdin.readline

def dijkstra(start_v):
    hq = []
    heapq.heappush(hq, [0, start_v])
    distance[start_v] = 0

    while hq:
        now_dis, now_v = heapq.heappop(hq)
        if now_dis > distance[now_v]:
            continue

        for next_v in graph[now_v]:
            next_dis = now_dis + next_v[0]
            if next_dis < distance[next_v[1]]:
                distance[next_v[1]] = next_dis
                heapq.heappush(hq, [next_dis, next_v[1]]) 



if __name__ == "__main__":
    INF = 9876543210
    
    N, E = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        _v1, _v2, c = map(int, input().split())
        graph[_v1].append([c, _v2])
        graph[_v2].append([c, _v1])

    v1, v2 = map(int, input().split())

    min_dis = [9876543210, 9876543210]

    # 1 -> v1
    distance = [INF] * (N + 1)
    distance[1] = 0
    dijkstra(1)

    if min_dis == INF:
        print(-1)
        exit(0)
    
    # 1 -> v2
    

    # v1 -> v2, 
    distance = [INF] * (N + 1)
    
    distance[point_1] = min_dis
    dijkstra(point_1)

    if distance[point_2] == INF:
        print(-1)
        exit(0)

    min_dis += distance[point_2]

    # v1 or v2 -> N
    distance = [INF] * (N + 1)
    dijkstra(point_2)

    if distance[N] == INF:
        print(-1)
        exit(0)
    
    min_dis += distance[N]

    print(min_dis)
