# 1351
# 그저 재귀를 돌려 풀어보았으나, 시간초과가 떴음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
def solution(a,b):
    if a == 0 and b == 0:
        return 2
    else:
        if a==0:
            return 1 + solution(b//P, b//Q)
        if b==0:
            return solution(a//P,a//Q) + 1
    return solution(a//P,a//Q) + solution(b//P, b//Q)

    

N,P,Q = map(int,input().split())

if N == 0:
    print(1)
else:
    print(solution(N//P, N//Q))
"""

# N이 최대 10^12이기 때문 dp를 활용해 시간복잡도를 줄여야 함
# 최악의 경우 N = 10^12 , P,Q = 2


def dp(N):
    if N in graph: # 만약 graph[N]을 이미 구했던 적이 있어, 그래프에 저장되어 있다면,
        return graph[N] # 계산 필요없이 바로 return
    else: # graph[N]을 구한 적이 없어, 그래프에 저장되어 있지 않다면,
        graph[N] = dp(N//P) + dp(N//Q) # 재귀를 돌려 graph(N) 구한 후, graph에 저장
        return graph[N]


graph = {} # 그래프 : dp로 활용할 것. 딕셔너리로 선언
graph[0] = 1 # A0 = 1 

N,P,Q = map(int,input().split())

print(dp(N))



