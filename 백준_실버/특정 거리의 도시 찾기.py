# 18352
import sys
import heapq

input = sys.stdin.readline

def dijkstra(start_v):
    hq = []
    heapq.heappush(hq, [0, start_v])

    while hq:
        now_dis, now_v = heapq.heappop(hq)

        for next_v in city[now_v]:
            if distance[next_v] > now_dis + 1:
                distance[next_v] = now_dis + 1
                heapq.heappush(hq, [distance[next_v], next_v])
    

if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    
    city = [[] for _ in range(N + 1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        city[v1].append(v2)
    
    INF = 10**6 + 1
    distance = [INF] * (N + 1)
    distance[X] = 0

    dijkstra(X)

    is_exist = False

    for i in range(1, N + 1):
        if distance[i] == K:
            print(i, end=" ")
            is_exist = True
    
    if not is_exist:
        print(-1)