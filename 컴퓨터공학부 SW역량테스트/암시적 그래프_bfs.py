from collections import deque

def isValid(r, c):
    return 0 <= r < row_len and 0 <= c < col_len and grid[r][c] == 1

def bfs(grid):

    visited = [[False] * col_len for _ in range(row_len)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append(0, 0)
    visited[0][0] = True
    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if (next_r >= 0 and next_r < row_len) and (next_c >= 0 and next_c < col_len):
                if grid[next_r][next_c] == 1:
                    if not visited[next_r][next_c]:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True

grid = [
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 1]
]

row_len = len(grid)
col_len = len(grid[0])

bfs(grid)