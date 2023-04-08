# 23631

# 시간초과 이유 : 점화식을 무식하게 사용. 10**7번 재귀를 돌다보니 불가피했음

# import sys
# import math

# sys.setrecursionlimit(10**9) # 최대 재귀호출 횟수 증가
# input = sys.stdin.readline

# def solution(start, K):
#     global cnt,sum,loc
#     if (sum + (cnt + 1) * K) >= N:
#         return
#     cnt += 1
#     sum += cnt * K
#     loc += (-1)**(cnt + 1) * cnt * K
#     # print(cnt, end=" ")
#     # print(sum, end=" ")
#     # print(loc)
    
#     solution(loc, K)




# # T = int(input()) 


# # for _ in range(T):
# cnt = 0 # 몇턴째 뛰고있는 것인지도 밝혀줄 것.
# sum = 0 # 현재 턴까지 총 뛴 거리를 담을 변수
# loc = 0 # cnt만큼 뛰었을 때 도착 위치
# # N-1만큼 뛸 것이고, 매 사이클마다 K를 더한만큼 뛰는 거리가 증가할 것.
# # R방향으로 시작하여 L,R방향 계속 스위치

# N,K = map(int,input().split())
# solution(0, K) # 초기 매개변수 : 시작점 좌표 0, R방향으로 뛰어 도착한 K
# left = N - sum
# if cnt == 0:
#     answer = 0 + N - 1
#     print(f"{answer} R")
#     exit()
# if loc > 0:
#     answer = loc - left + 1
#     print(f"{answer} L")
# else: 
#     answer = loc + left - 1
#     print(f"{answer} R")


# 이진 탐색을 이용한 문제 풀이가 핵심 : 시간복잡도 O(lg N) 
# 참고 : https://lbdiaryl.tistory.com/222

""" 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법 """
""" 리스트 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘 """ 
""" 좁혀가며 찾아야 하는 데이터 : N-1만큼의 거리를 넘기기 직전 점프해서 도착한 좌표 위치 """
    
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def solution(start, end):
    if start>=end: # start가 end보다 크면 start지점이 마지막 점프로 도착했을 때의 총 점프 횟수로, return
        return start

    mid = (start + end) // 2 # 중간값 : mid

    if mid * (mid + 1) * K >= 2 * N: # mid만큼 뛰었을 때, 공차가 K인 경우 총 뛴 거리가 N보다 크거나 같다면
        return solution(start , mid) # 구하려는 총 점프 횟수는 start이상 mid 이하일 것이다.
    else:                            # mid만큼 뛰었을 때, 공차가 K인 경우 총 뛴 거리가 N보다 작다면
        return solution(mid+1 , end) # 구하려는 총 점프 횟수는 mid 초과 end 이하일 것이다.
    




T = int(input()) 


for _ in range(T):

    sum = 0 # 현재 턴까지 총 뛴 거리를 담을 변수

    start = 0
    # 최대 N이 10**7, 최소 K가 1일 때, 최대 재귀 횟수를 end변수에 대입
    end = 4500 # 4500*(4501)/2 ~~ 10**7
    # N-1만큼 뛸 것이고, 매 사이클마다 K를 더한만큼 뛰는 거리가 증가할 것.
    # R방향으로 시작하여 L,R방향 계속 스위치

    N,K = map(int,input().split())
    arrive = solution(start, end) # 초기 매개변수 : 0~5000 사이이므로 start : 0 , end : 5000
    # 마지막 점프로 도착했을 때의 총 점프 횟수를 arrive 변수에 저장
    
    sum = arrive * (arrive + 1) // 2 # 공차가 있는 수열의 합 점화식

    if arrive % 2 != 0: # 총 점프 횟수가 홀수 : 마지막 점프 후, 도착 위치는 양수이다.
        answer = K * (arrive // 2 + 1)
        answer += (N-1) - sum * K
        print(f"{answer} R")
    else:               # 총 점프 횟수가 짝수 : 마지막 점프 후, 도착 위치는 음수이다.
        answer = -1 * K * (arrive // 2) 
        answer -= (N-1) - sum * K # 
        print(f"{answer} L")



    
        