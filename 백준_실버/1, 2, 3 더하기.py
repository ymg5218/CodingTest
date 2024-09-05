# 9095

if __name__ == "__main__":
    # 기저 조건 n = 1 ~ 3, 0번째 인덱스는 더미 인덱스
    dp = [0, 1, 2, 4]
    # n은 최대 10 이므로 n = 10까지 dp를 채워줌
    for i in range(4, 11):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    T = int(input())
    for _ in range(T):
        print(dp[int(input())])