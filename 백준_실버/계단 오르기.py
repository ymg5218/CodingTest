# 2579

import sys
input = sys.stdin.readline

def solution():
    dp = []

    # dp 각 요소의 0번째 인덱스 : 현재 계단이 연속 1개 째 밟은 상태
    # dp 각 요소의 1번째 인덱스 : 현재 계단이 연속 2개 째 밟은 상태
    
    # dp[0] : 시작점
    dp.append([0, 0])

    # dp[1] : 첫 번째 계단
    dp.append([stair[1], 0])

    for idx in range(2, n+1):
        dp.append([])
        # 0번째 인덱스 : 현재 계단이 연속 1개 째 밟은 상태 = 계단을 2개 뛰어 넘은 상태의 최댓값
        dp[idx].append(max(dp[idx - 2]) + stair[idx])

        # 1번째 인덱스 : 현재 계단이 연속 2개 째 밟은 상태 = 이전 게단의 최댓값 중, 계단 1개를 연속으로 밟은 값에서만 따져야 함
        dp[idx].append(dp[idx - 1][0] + stair[idx])
    
    print(max(dp[-1]))

if __name__ == "__main__":
    n = int(input())

    stair = [0] # 0번째 인덱스는 더미 값
    for _ in range(n):
        stair.append(int(input()))
    
    solution()