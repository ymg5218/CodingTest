# 1012
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(now_x, now_y):
    if visited[now_x][now_y]:
        return
    visited[now_x][now_y] = True
    
    next_v = []
    
    for i in range(4):
        if is_valid(now_x + dy[i], now_y + dx[i]):
            next_v.append([now_x + dy[i], now_y + dx[i]])
    
    for v in next_v:
        dfs(v[0], v[1])


def is_valid(_x, _y):
    if _x < 0 or _x >= N or _y < 0 or _y >= M:
        return False
    elif field[_x][_y] == 0:
        return False
    return True

if __name__ == "__main__":
    T = int(input())

    # 오른쪽, 아래, 왼쪽, 위
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(T):
        M, N, K = map(int, input().split())
        
        cnt = 0

        field = [[0 for _ in range(M)] for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            # y = 열, x = 행
            y, x = map(int, input().split())
            field[x][y] = 1
        for y_idx in range(M):
            for x_idx in range(N):
                if not visited[x_idx][y_idx] and field[x_idx][y_idx] == 1:
                    dfs(x_idx, y_idx)
                    cnt += 1
        
        print(cnt)
        