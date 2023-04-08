# 13023
'''
오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.             A
B는 C와 친구다.      ==       B
C는 D와 친구다.                 C
D는 E와 친구다.                   D
                                   E

위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성
'''

# 인원이 N명일 때, 그래프의 깊이가 N-1이면 print : 1 인 문제 (루트노드는 깊이 0으로 간주)
# 라고 생각했으나, 문제 그대로, A-B-C-D-E 인 관계가 한 경우라도 있으면 print : 1
# 즉, 깊이가 4인 경우가 하나라도 있는가를 알아내는 문제이다.

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N, M = map(int,input().split()) # N : 사람의 수 , M : 친구 관계의 수

graph = [[]for _ in range(N)] # 그래프 틀 선언
visited = [False] * N
# 상호 연결관계 입력
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프를 dfs를 이용해 깊이를 탐색, 깊이가 N-1이면 print : 1 , 아니면 print : 0

def dfs(node,depth):
    if depth == 4 : # 깊이가 4인 경우가 존재하면 print : 1 이후 바로 종료
        print(1)
        exit(0)
    for child in graph[node]: # 현재 탐색중인 노드의 자식노드들 탐색
        if visited[child] == True: # 만약 자식노드가 방문했던 노드라면
            continue 
        visited[child] = True # 방문했으니 True
        dfs(child,depth + 1) # 자식노드로 한단계 깊게 탐색들어가니 depth + 1
        visited[child] = False # callback하며 visited 초기화

for start in range(N):
    visited[start] = True # 모든 노드를 루트노드로 가정, 하나하나 dfs
    dfs(start,0) # 초기 매개변수 : 루트노드,초기깊이 0
    visited[start] = False # 다시 돌아왔다는 뜻 : 얘가 root일 땐 depth = 4 인 경우가 없었음. 다시 초기화

print(0) # depth = 4인 case가 없다면 print : 0
