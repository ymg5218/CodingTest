# 1463

def solution():
    # dp 0번째 인덱스는 더미 값
    dp = [-1]
    # dp 1번째 인덱스는 기저 값 (1로 1을 만드는데 필요한 연산 횟수 : 0)
    dp.append(0)

    for num in range(2, N + 1):
        if num % 3 == 0 and num % 2 == 0:
            dp.append(min(dp[num // 3] + 1 , dp[num // 2] + 1 , dp[num - 1] + 1))
        elif num % 3 == 0:
            dp.append(min(dp[num // 3] + 1 , dp[num - 1] + 1))
        elif num % 2 == 0:
            dp.append(min(dp[num // 2] + 1 , dp[num - 1] + 1))
        else:
            dp.append(dp[num - 1] + 1)
    
    return dp[-1]
    
if __name__ == "__main__":
    N = int(input())

    print(solution())