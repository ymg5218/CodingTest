# https://leetcode.com/problems/climbing-stairs/submissions/

# 가정 : 피보나치 수열로 증가하는 그림을 보인다

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1 : 1, 2 : 2}
        for idx in range(3,n+1):
            dp[idx] = dp[idx - 2] + dp[idx - 1]
        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(3))

















































































