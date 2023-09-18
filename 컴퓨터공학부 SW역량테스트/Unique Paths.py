# https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # m x n 사이즈의 2차원 dp 선언
        dp = [[-1] * n for _ in range(m)]

        # 0행, 0열 1로 초기값 세팅
        for row in range(m):
            dp[row][0] = 1
        for col in range(n):
            dp[0][col] = 1

        # 점화식 : dp[m][n] = dp[m - 1][n] + dp[m][n - 1]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        # 2차원 dp 마지막 인덱스 값 출력
        return dp[m - 1][n - 1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3,7))
