# 1926
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_row, start_col):
    size = 0

    queue = deque()
    queue.append([start_row, start_col])
    size += 1
    board[start_row][start_col] = 0

    # 동 남 서 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    while queue:
        now_row, now_col = queue.popleft()
        for i in range(4):
            next_row, next_col = now_row + d_row[i], now_col + d_col[i]
            if 0 <= next_row < n and 0 <= next_col < m:
                if board[next_row][next_col] == 1:
                    size += 1
                    board[next_row][next_col] = 0
                    queue.append([next_row, next_col])

    return size


def solution():
    cnt = 0
    max_size = 0
    
    for row in range(n):
        for col in range(m):
            if board[row][col] == 1:
                cnt += 1
                max_size = max(max_size, bfs(row, col))

    print(cnt)
    print(max_size)
if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    
    solution()
    