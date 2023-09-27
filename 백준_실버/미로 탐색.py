# 2178

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    # 오른쪽, 아래, 왼쪽, 위쪽
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    next_queue = deque()

    cnt = 1

    while queue:
        while queue:
            now = queue.popleft()
            for idx in range(4):
                if isValid(now, dx[idx], dy[idx]):
                    next_v = [now[0] + dy[idx], now[1] + dx[idx]]
                    if next_v == [N - 1, M - 1]:
                        cnt += 1
                        print(cnt)
                        exit()
                    next_queue.append(next_v)
                    visited[now[0] + dy[idx]][now[1] + dx[idx]] = True
        while next_queue:
            queue.append(next_queue.popleft())
        cnt += 1
    

def isValid(now, dx, dy):
    if 0 <= now[0] + dy < N and 0 <= now[1] + dx < M:
        if board[now[0] + dy][now[1] + dx] == '1' and visited[now[0] + dy][now[1] + dx] == False:
            return True
        else:
            return False
    return False

if __name__ == "__main__":
    N, M = map(int,input().split())
    board = []
    visited = [ [False] * M for _ in range(N)]
    for _ in range(N):
        board.append(input().strip())
    
    bfs()
