# 2747

N = int(input())

dp = [0, 1]

for i in range(2, N + 1):
    dp.append(dp[i - 2] + dp[i - 1])

print(dp[-1])