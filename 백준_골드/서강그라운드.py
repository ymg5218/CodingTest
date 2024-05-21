# 14938
import sys
import heapq

input = sys.stdin.readline


def dijkstra(start_v):
    INF = m + 1
    distance = [INF] * (n + 1)
    distance[start_v] = 0

    hq = []
    heapq.heappush(hq, [0, start_v])

    while hq:
        now_dis, now_v = heapq.heappop(hq)

        for next_dis, next_v in field[now_v]:
            if next_dis < distance[next_v]:
                if now_dis + next_dis <= m:
                    distance[next_v] = now_dis + next_dis
                    heapq.heappush(hq, [distance[next_v], next_v])

    cnt = 0

    for idx in range(1, n + 1):
        if distance[idx] < INF:
            cnt += items[idx]

    return cnt


if __name__ == "__main__":
    n, m, r = map(int, input().split())

    items = [-1]
    temp = list(map(int, input().split()))
    items.extend(temp)

    field = [[] for _ in range(n + 1)]

    for _ in range(r):
        v1, v2, dis = map(int, input().split())
        field[v1].append([dis, v2])
        field[v2].append([dis, v1])

    max_cnt = 0

    for i in range(1, n+1):
        max_cnt = max(max_cnt, dijkstra(i))

    print(max_cnt)