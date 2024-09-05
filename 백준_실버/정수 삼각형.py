# 1932
import sys
input = sys.stdin.readline

def solution():
    dp = [[] for _ in range(n)]
    dp[0].append(table[0][0])

    for row in range(1, n):
        for col in range(row + 1):
            if col == 0:
                dp[row].append(dp[row - 1][col] + table[row][col])
            elif col == row:
                dp[row].append(dp[row - 1][col - 1] + table[row][col])
            else:
                dp[row].append(max(dp[row - 1][col - 1], dp[row - 1][col]) + table[row][col])

    print(max(dp[-1]))

if __name__ == "__main__":
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))

    solution()