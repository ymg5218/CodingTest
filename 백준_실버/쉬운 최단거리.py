# 14940
from collections import deque
import sys

input = sys.stdin.readline

def bfs(start_row, start_col):
    queue = deque()

    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    queue.append([start_row, start_col])
    result[start_row][start_col] = 0
    nowSeq = 1

    next_v = []

    while queue:
        while queue:
            nowRow, nowCol = queue.popleft()
            for i in range(4):
                nextRow = nowRow + d_row[i]
                nextCol = nowCol + d_col[i]
                if 0 <= nextRow < n and 0 <= nextCol < m:
                    if board[nextRow][nextCol] == 0:
                        result[nextRow][nextCol] = 0
                    elif result[nextRow][nextCol] == -1 and board[nextRow][nextCol] == 1:
                        result[nextRow][nextCol] = nowSeq
                        next_v.append([nextRow, nextCol])
        while next_v:
            queue.append(next_v.pop())
        nowSeq += 1

    for row in range(n):
        print(*result[row])

if __name__ == "__main__":
    n, m = map(int, input().split())

    start_row = -1
    start_col = -1

    board = []
    result = [[-1 for _ in range(m)] for _ in range(n)]
    for row in range(n):
        temp = list(map(int, input().split()))
        for col in range(m):
            if temp[col] == 2:
                start_row = row
                start_col = col
            elif temp[col] == 0:
                result[row][col] = 0
        board.append(temp)

    bfs(start_row, start_col)