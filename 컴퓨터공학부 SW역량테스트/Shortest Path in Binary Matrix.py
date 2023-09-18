# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_length = -1

        col_len = len(grid[0])
        row_len = len(grid)
        visited = [[False] * col_len for _ in range(row_len)]
        
        #    동  서  남  북 북동 남동 북서 남서
        dr = [1, -1, 0,  0,  1,  1,  -1,  -1]
        dc = [0, 0,  1, -1,  1, -1,   1,  -1]

        # 시작점
        start_v = (0,0)
        # 도착점
        dest_v = (row_len - 1, col_len - 1)
        
        # Flow (feat. BFS)
        '''
         1. start_v 예약하기
         2. while queue 큐 소진시까지 반복하기
            2-1. 방문하기
            2-2. next_v 예약하기
        '''
        # 1. start_v 예약하기
        q = deque()
        # (0,0)이 0일 때 -> (0,0)이 1일수도 있는 예외 존재
        if grid[0][0] == 0:
            # 시작점 : 0,0
            # 거리 최소값은 1
            q.append((0,0,1))
            visited[0][0] = True

        # 2. while queue 큐 소진시까지 반복하기
        while q:
            # 2-1. 방문하기
            cur_r, cur_c, cur_length = q.popleft()
            # 만약 방문한 지점이 도착점이라면 최단거리 출력 return
            if cur_r == row_len - 1 and cur_c == col_len - 1:
                shortest_length = cur_length
                return cur_length

            # 2-2. next_v 예약하기
            for idx in range(8):
                next_r = cur_r + dr[idx]
                next_c = cur_c + dc[idx]
                if 0 <= next_r < row_len and 0 <= next_c < col_len and grid[next_r][next_c] == 0:
                    if not visited[next_r][next_c]:
                        q.append((next_r, next_c, cur_length + 1))
                        visited[next_r][next_c] = True

        return shortest_length
            
        
if __name__ == "__main__":
    grid = [
        [0,0,0],
        [1,1,0],
        [1,1,0]
    ]

    solution = Solution()
    print(solution.shortestPathBinaryMatrix(grid))