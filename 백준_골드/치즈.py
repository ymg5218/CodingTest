# 2638

import sys
from collections import deque

input = sys.stdin.readline

# 해당 칸이 외부공기인지 확인하는 메소드
def isValid(row, col, visited):
    if 0 <= row < N and 0 <= col < M:
        if not visited[row][col] and board[row][col] == 0:
            return True
    
    return False

def bfs(row, col, visited):
    # 동, 남, 서, 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    queue = deque()
    queue.append([row, col])
    visited[row][col] = True

    while queue:
        now_v = queue.popleft()
        now_row = now_v[0]
        now_col = now_v[1]

        for i in range(4):
            next_row = now_row + d_row[i]
            next_col = now_col + d_col[i]
            if isValid(next_row, next_col, visited):
                queue.append([next_row, next_col])
                visited[next_row][next_col] = True
    
    return visited

def solution():
    global cnt
    time = 0

    # 동, 남, 서, 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    while cnt > 0:
        # 매 사이클마다 bfs 수행, 노출되어있는 공간을 담을 opened 선언 및 세팅
        opened = bfs(0, 0, [[False for _ in range(M)] for _ in range(N)])
        
        will_melt = []

        for row in range(N):
            for col in range(M):
                if board[row][col] == 1:
                    # 노출된 면 개수
                    open_cnt = 0
                    for i in range(4):
                        if opened[row + d_row[i]][col + d_col[i]]:
                            open_cnt += 1
                    if open_cnt >= 2:
                        will_melt.append([row, col])
        
        while will_melt:
            melt = will_melt.pop()
            board[melt[0]][melt[1]] = 0
            cnt -= 1
        
        time += 1

    return time

if __name__ == "__main__":
    N, M = map(int, input().split())

    board = []
    
    cnt = 0

    for _ in range(N):
        row = list(map(int, input().split()))
        for x in row:
            if x == 1:
                cnt += 1
        board.append(row)
    
    print(solution())