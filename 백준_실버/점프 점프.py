# 11060

'''
1. 입력값들을 입력받고, dp를 N 크기만큼 선언한다. 후 dp 내 모든 요소 1001(최댓값)으로 초기화
2. 미로 배열(A)의 첫 번째 인덱스부터 하나씩 탐색하며, 해당 칸에서 점프해 도달할 수 있는 칸을 모두 비교하며 전진한다.
    이 때, dp를 사용하며, 점프하여 도착한 위치 인덱스의 dp값과, 해당 인덱스의 기존 dp 값과 비교하여 "더 작은 최솟값"으로 치환한다.
3. 계속 반복하여 마지막 미로까지 전진한다
'''

'''
자세한건 손그림으로 설명하였음
'''

N = int(input())

MAX = 1001 # 최소값을 채택하기 위해 임의의 최댓값 MAX 선언

A = list(map(int,input().split()))

dp = [MAX for _ in range(N)] # 최대값으로 초기화

dp[0] = 0 # 첫 번째 인덱스는 출발점이니 0으로 재선언

for i in range(N):
    for j in range(1, A[i] + 1): # 만약 A[i]가 3이라면, dp[i+1], dp[i+2], dp[i+3]을 참조하게 할 것이다.
        if i+j >= N: # dp[i+j]가 범위 밖을 참조하려 한다면 break
            break
        dp[i+j] = min(dp[i+j],dp[i] + 1) # dp[i+j]와, dp[i] + 1 을 비교, 도착할 수 있는 더 적은 점프 회수를 채택한다.

if dp[-1] == MAX: # dp에서 마지막 인덱스 값을 한 번도 참조하지 못했다면 = 마지막까지 도달하지 못했다면
    print(-1) # -1 출력
else:
    print(dp[-1]) # dp에서 마지막 인덱스 값을 출력하면 정답.
