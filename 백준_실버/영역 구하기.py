import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_row, start_col):
    cnt = 0
    queue = deque()

    queue.append([start_row, start_col])
    board[start_row][start_col] = 1
    cnt += 1

    # 동, 남, 서, 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    while queue:
        now_row, now_col = queue.popleft()
        for i in range(4):
            next_row, next_col = now_row + d_row[i], now_col + d_col[i]
            if 0 <= next_row < N and 0 <= next_col < M:
                if board[next_row][next_col] == 0:
                    board[next_row][next_col] = 1
                    queue.append([next_row, next_col])
                    cnt += 1
    
    return cnt


def solution():
    result = []

    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                result.append(bfs(row, col))
    print(len(result))
    print(*(sorted(result)))


if __name__ == "__main__":
    M, N, K = map(int, input().split())

    # 2차원 배열에서는 왼쪽 위가 [0, 0] 이지만, 문제에서는 왼쪽 아래가 [0, 0] 이다.
    # board를 시계방향으로 90도 회전시켜 풀어도 문제 해결에 지장을 주지 않는다고 판단
    board = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        y1, x1, y2, x2 = map(int, input().split())
        now_row = y1
        for row in range(y2 - y1):
            now_col = x1
            for col in range(x2 - x1):
                board[now_row][now_col] = 1
                now_col += 1
            now_row += 1
    
    solution()