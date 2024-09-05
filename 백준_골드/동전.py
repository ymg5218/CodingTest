# 9084

import sys
input = sys.stdin.readline

def solution():
    dp = [0 for _ in range(M + 1)]

    for c in range(N):
        now_coin = coin[c]
        if M >= now_coin:
            dp[now_coin] += 1
        for col in range(now_coin, M + 1):
            if M >= now_coin:
                dp[col] += dp[col - now_coin]

    print(dp[-1])

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())

        coin = list(map(int, input().split()))

        M = int(input())


        solution()