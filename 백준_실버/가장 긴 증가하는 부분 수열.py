# 11053

def solution():
    dp = [1 for _ in range(N)]

    for idx_1 in range(N):
        for idx_2 in range(idx_1):
            if A[idx_2] < A[idx_1]:
                dp[idx_1] = max(dp[idx_1] , dp[idx_2] + 1)
    
    print(max(dp))


if __name__ == "__main__":
    N = int(input())

    A = list(map(int, input().split()))

    solution()