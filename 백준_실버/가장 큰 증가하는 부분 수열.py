# 11055

def solution():
    # idx 0 : LIS 길이
    # idx 1 : LIS 구성 요소
    # idx 2 : LIS 구성 요소 합
    dp = [[1, [A[i]], A[i]] for i in range(N)]
    
    for idx_1 in range(1, N):
        for idx_2 in range(idx_1):
            if A[idx_2] < A[idx_1]:
                if dp[idx_1][0] < dp[idx_2][0] + 1 and dp[idx_1][2] < A[idx_1] + dp[idx_2][2]:
                    dp[idx_1][0] = dp[idx_2][0] + 1
                    dp[idx_1][1] = dp[idx_2][1][:]
                    dp[idx_1][1].append(A[idx_1])
                    dp[idx_1][2] = sum(dp[idx_1][1])
    
    max_sum = 0
    for re in dp:
        if re[2] > max_sum:
            max_sum = re[2]
    
    return max_sum
                

if __name__ == "__main__":
    N = int(input())

    A = list(map(int, input().split()))

    print(solution())