# https://leetcode.com/problems/keys-and-rooms/

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        start_v = 0
        rooms_cnt = len(rooms)
        self.dfs(rooms, visited, start_v)
        
        if rooms_cnt != len(visited):
            return False
        else:
            return True
        
    def dfs(self, rooms, visited, now_v):
        visited[now_v] = True
        for next_v in rooms[now_v]:
            if next_v not in visited:
                self.dfs(rooms, visited, next_v)
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))