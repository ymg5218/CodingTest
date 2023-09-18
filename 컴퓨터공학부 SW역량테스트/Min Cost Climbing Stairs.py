# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {0 : cost[0]}
        dp[1] = cost[1]
        length = len(cost)

        for idx in range(2, length):
            dp[idx] = min(dp[idx - 1] + cost[idx], dp[idx - 2] + cost[idx])

        return min(dp[length - 1], dp[length - 2])

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([10,15,20]))