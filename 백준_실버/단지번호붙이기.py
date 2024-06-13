# 2667
import sys
from collections import deque
input = sys.stdin.readline

def isValid(row, col):
    if 0 <= row < N and 0 <= col < N:
        if board[row][col] == "1" and not visited[row][col]:
            return True
    
    return False


def bfs(start_row, start_col):
    cnt = 0

    # 동 남 서 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    queue = deque()
    queue.append([start_row, start_col])
    visited[start_row][start_col] = True

    while queue:
        now_row, now_col = queue.popleft()
        cnt += 1
        for i in range(4):
            next_row = now_row + d_row[i]
            next_col = now_col + d_col[i]
            if isValid(next_row, next_col):
                visited[next_row][next_col] = True
                queue.append([next_row, next_col])

    return cnt

if __name__ == "__main__":
    N = int(input())
    board = []
    
    for _ in range(N):
        board.append(input())
    
    visited = [[False for _ in range(N)] for _ in range(N)]

    result = []
    result_cnt = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == "1" and not visited[row][col]:
                result.append(bfs(row, col))
                result_cnt += 1
    
    result.sort()
    print(result_cnt)
    for re in result:
        print(re)
    