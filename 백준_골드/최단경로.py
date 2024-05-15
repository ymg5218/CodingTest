# 1753
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start_v):
    hq = []
    heapq.heappush(hq, (0, start_v))

    while hq:
        now_dis, now_node = heapq.heappop(hq)
        
        if dis[now_node] < now_dis:
            continue

        for next_v, distance in graph[now_node]:
            cost = now_dis + distance
            if cost < dis[next_v]:
                dis[next_v] = cost
                heapq.heappush(hq, (cost, next_v))



if __name__ == "__main__":
    INF = 10 * 20000 + 1

    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    
    start_v = int(input())
    
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        graph[v1].append([v2, w])
    
    dis = [INF for _ in range(V+1)]
    dis[start_v] = 0

    dijkstra(start_v)

    for i in range(1, V + 1):
        if dis[i] == INF:
            print("INF")
        else:
            print(dis[i])