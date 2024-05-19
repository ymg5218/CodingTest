# 2468
import sys
from collections import deque

input = sys.stdin.readline

def isValid(row, col, rain):
    global visited
    if 0 <= row < N and 0 <= col < N:
        if city[row][col] > rain:
            if not visited[row][col]:
                return True

    return False

def bfs(start_row, start_col, rain):
    global visited
    # 동, 남, 서, 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    queue = deque([])
    queue.append([start_row, start_col])
    visited[start_row][start_col] = True

    while queue:
        now = queue.popleft()
        for i in range(4):
            next_row = now[0] + d_row[i]
            next_col = now[1] + d_col[i]
            if isValid(next_row, next_col, rain):
                visited[next_row][next_col] = True
                queue.append([next_row, next_col])



if __name__ == "__main__":
    N = int(input())

    city = []
    for _ in range(N):
        city.append(list(map(int, input().split())))

    max_safezon = 1
    for i in range(1, 100):
        visited = [[False for _ in range(N)]for _ in range(N)]
        cnt = 0
        for row in range(N):
            for col in range(N):
                if city[row][col] > i and visited[row][col] == False:
                    bfs(row, col, i)
                    cnt += 1

        max_safezon = max(max_safezon, cnt)


    print(max_safezon)
