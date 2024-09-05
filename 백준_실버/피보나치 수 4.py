# 10826

n = int(input())

dp = [0, 1]

for idx in range(2, n + 1):
    dp.append(dp[idx - 2] + dp[idx - 1])

print(dp[n])