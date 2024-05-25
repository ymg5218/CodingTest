# 2775

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[i for i in range(n + 1)]]

    for row in range(1, k + 1):
        temp = [0]
        for col in range(1, n + 1):
            temp.append(temp[-1] + dp[row - 1][col])
        dp.append(temp)
    
    print(dp[k][n])

    
