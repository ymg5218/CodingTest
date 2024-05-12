# 24463
import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

def isValid(row, col): 
    if 0 <= row < N and 0 <= col < M and maze[row][col] == "@":
        return True
    return False
    

def dfs(now_point):
    if now_point == exit[1]:
        return True

    for i in range(4):
        # 갈 수 있는 좌표
        next_row, next_col = now_point[0] + d_row[i], now_point[1] + d_col[i]
        if isValid(next_row, next_col):
            maze[next_row][next_col] = "."
            if dfs([next_row, next_col]):
                return True 
            # True를 반환하지 못함 : 끝까지 못갔음
            maze[next_row][next_col] = "@"
    
    return False

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    maze = []

    exit = []
    
    for i in range(N):
        maze_row = list(input())
        # 출구 찾기 -> 미로의 위/아랫면에 존재하는지
        for j in range(M):
            if maze_row[j] == ".":
                if j == 0 or j == M - 1 or i == 0 or i == N - 1:
                    exit.append([i, j])
                maze_row[j] = "@"
        maze.append(maze_row)

        
    # 오른쪽, 아래쪽, 왼쪽, 위쪽
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    # 출구 중 하나를 입구로 선택하여 dfs 시작
    maze[exit[0][0]][exit[0][1]] = "."
    dfs(exit[0])

    for i in range(N):
        for j in range(M):
            print(maze[i][j], end="")
        print()

    
        