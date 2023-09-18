# https://leetcode.com/problems/network-delay-time/description/?orderBy=most_votes

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 구현
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))

        # 다익스트라 알고리즘 구현
        costs = {}
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_node))
        

        # 방문 못한 노드 찾기
        for node in range(1, n + 1):
            if node not in costs:
                return -1

        # 최소값 중에서 최대값 구하기
        return max(costs.values())
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))