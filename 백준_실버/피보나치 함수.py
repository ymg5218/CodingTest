# 1003

def fibo(end_num, N):
    if end_num >= N:
        result = [dp[N][0], dp[N][1]]
    else:
        start_num = end_num
        for i in range(start_num + 1, N + 1):
            dp.append([dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]])
        result = [dp[-1][0], dp[-1][1]]
        end_num = N
    return end_num, result

if __name__ == "__main__":
    T = int(input())

    dp = [[1, 0], [0, 1]]
    end_num = 1

    for _ in range(T):
        N = int(input())
        end_num, result = fibo(end_num, N)
        for idx in range(2):
            print(result[idx], end=" ")
        print()