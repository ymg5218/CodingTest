# 17129

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_row, start_col):
    queue = deque()
    # 동 남 서 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    queue.append([start_row, start_col])
    board[start_row][start_col] = "1"

    distance = 1
    while queue:
        for _ in range(len(queue)):
            now_row, now_col = queue.popleft()
            for i in range(4):
                next_row, next_col = now_row + d_row[i], now_col + d_col[i]
                if 0 <= next_row < n and 0 <= next_col < m and board[next_row][next_col] != "1":
                    if board[next_row][next_col] in ("3", "4", "5"):
                        print("TAK")
                        print(distance)
                        return
                    else:
                        queue.append([next_row, next_col])
                        board[next_row][next_col] = "1"
        distance += 1


    print("NIE")


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for row in range(n):
        now = list(input())
        board.append(now)
        for col in range(m):
            if now[col] == "2":
                start_row, start_col = row, col


    bfs(start_row, start_col)



