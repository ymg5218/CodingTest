# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global row_len, col_len, visited, dr, dc

        row_len, col_len = len(grid), len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]
        dr = [0, 1 ,0 ,-1]
        dc = [1, 0, -1, 0]
        cnt = 0

        # grid를 모두 순회하며, 방문한 적 없는 1이면 해당 지점을 시작점으로 지정.
        # dfs를 시작한 지점이 n개라면, 독립적인 그래프가 n개라는 뜻
        for i in range(row_len):
            for j in range(col_len):
                if visited[i][j] != True and grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

    def isValid(self, grid, r, c):
        return 0 <= r < row_len and 0 <= c < col_len and grid[r][c] == "1"
        
    def dfs(self, grid, r, c):
        visited[r][c] = True
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            if self.isValid(grid, next_r, next_c):
                if not visited[next_r][next_c]:
                    self.dfs(grid, next_r, next_c)

if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    solution = Solution()
    print(solution.numIslands(grid))