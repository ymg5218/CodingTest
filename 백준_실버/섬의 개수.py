# 4963
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_row, start_col):
    # 동, 동남, 남, 남서, 서, 북서, 북, 북동
    d_row = [0, 1, 1, 1, 0, -1, -1, -1]
    d_col = [1, 1, 0, -1, -1, -1, 0, 1]

    queue = deque()
    queue.append([start_row, start_col])
    visited[start_row][start_col] = True

    while queue:
        now_row, now_col = queue.popleft()
        for i in range(8):
            next_row, next_col = now_row + d_row[i], now_col + d_col[i]
            if 0 <= next_row < h and 0 <= next_col < w:
                if not visited[next_row][next_col] and board[next_row][next_col] == 1:
                    queue.append([next_row, next_col])
                    visited[next_row][next_col] = True

if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break
        board = []
        visited = [[False for _ in range(w)] for _ in range(h)]
        for _ in range(h):
            board.append(list(map(int, input().split())))

        cnt = 0

        for row in range(h):
            for col in range(w):
                if board[row][col] == 1 and not visited[row][col]:
                    bfs(row, col)
                    cnt += 1
        print(cnt)