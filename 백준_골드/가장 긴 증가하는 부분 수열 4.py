# 14002

def solution():
    # dp를 2차원 배열로 선언.
    # 각 요소의 초기값은 => [ 1 , [A 배열의 각 인덱스 요소] ]
    dp = [ [1, [num]] for num in A ]

    # 모든 A배열 각 요소가 가장 마지막 요소인 경우를 탐색
    for idx_1 in range(N):
        # 조건에 만족하는 이전 dp 값들 중, 
        # 가장 큰 길이에 1을 더한 값을 해당 dp 인덱스의 0번째 인덱스 위치에 값 갱신
        # 가장 큰 길이일 때의 LIS 구성 요소에 현재 탐색 중인 수를 append한 배열을 헤당 dp 인덱스의 1번째 인덱스 위치 값으로 갱신
        for idx_2 in range(idx_1):
            if A[idx_2] < A[idx_1]:
                if dp[idx_1][0] < dp[idx_2][0] + 1:
                    dp[idx_1][0] = dp[idx_2][0] + 1
                    dp[idx_1][1] = dp[idx_2][1][:]
                    dp[idx_1][1].append(A[idx_1])
    
    max_len = 0
    result = []
    for i in range(N):
        if dp[i][0] > max_len:
            max_len = dp[i][0]
            result = dp[i][1][:]
    
    print(max_len)
    for re in result:
        print(re, end=" ")

if __name__ == "__main__":
    N = int(input())

    A = list(map(int, input().split()))

    solution()