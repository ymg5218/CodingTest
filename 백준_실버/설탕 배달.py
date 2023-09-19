# 2839

N = int(input())

dp = [
    [-1, -1],
    [-1, -1],
    [-1, -1]
]

cnt = 3

while(cnt <= N):
    if cnt == 3:
        dp.append([1, 0])
    
    elif cnt == 4:
        dp.append([-1, -1])

    elif cnt == 5:
        dp.append([0, 1])

    else:
        if dp[cnt - 3][0] == -1 and dp[cnt - 5][0] == -1:
            dp.append([-1, -1])

        elif dp[cnt - 3][0] == -1 and dp[cnt - 5][0] != -1:
            dp.append([dp[cnt - 5][0], dp[cnt - 5][1] + 1])

        elif dp[cnt - 3][0] != -1 and dp[cnt - 5][0] == -1:
            dp.append([dp[cnt - 3][0] + 1, dp[cnt - 3][1]])
        else:
            if (dp[cnt - 3][0] + 1 + dp[cnt - 3][1]) < (dp[cnt - 5][0] + dp[cnt - 5][1] + 1):
                dp.append([dp[cnt - 3][0] + 1, dp[cnt - 3][1]])
            else:
                dp.append([dp[cnt - 5][0], dp[cnt - 5][1] + 1])
    cnt += 1

if dp[-1][0] + dp[-1][1] < 0:
    print(-1)
else:
    print(dp[-1][0] + dp[-1][1])
        