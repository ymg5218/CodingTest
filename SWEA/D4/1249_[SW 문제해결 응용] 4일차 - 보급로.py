from collections import deque

def isValid(row, col):
    if 0 <= row < N and 0 <= col < N:
            return True
    return False

def bfs():
    min_cost = [[INF for _ in range(N)] for _ in range(N)]

    queue = deque([])
    queue.append([0, 0])
    min_cost[0][0] = int(map[0][0])

    while queue:
        now_row, now_col = queue.popleft()
        for i in range(4):
            next_row = now_row + d_row[i]
            next_col = now_col + d_col[i]
            if isValid(next_row, next_col):
                if min_cost[now_row][now_col] + int(map[next_row][next_col]) < min_cost[next_row][next_col]:
                    min_cost[next_row][next_col] = min_cost[now_row][now_col] + int(map[next_row][next_col])
                    queue.append([next_row, next_col])

    return min_cost[N - 1][N - 1]


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    map = []
    for _ in range(N):
        map.append(list(input()))

    # 동, 남, 서, 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    INF = 200 * 100



    print(f'#{t} {bfs()}')