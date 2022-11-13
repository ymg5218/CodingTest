# 1967

# 트리의 지름 구하기
# 각각의 노드 u,v가 있을 때, 이들 간의 거리를 d(u,v)라고 나타낼 수 있으며 최장거리(지름)은 MAX(d(u,v))
# 1. 임의의 노드 x를 잡는다
# 2. x에서 가장 먼 노드 y를 찾는다.
# 3. y에서 가장 먼 노드 z를 찾는다.
# 4. d(y,z)가 최장거리(지름)
# 참고 : https://blogshine.tistory.com/111

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node, dis): # 깊이우선탐색(노드번호, 탐색한 곳 까지의 거리)
    visited[node] = True # 탐색한 노드는 True로 지정
    for i in tree[node]: # node번째 노드와 연결된 노드 탐색
        temp_index = i[0] # 탐색중인 노드 번호 임시로 저장
        temp_dis = i[1] # 탐색중인 노드까지의 거리 임시로 저장
        if not visited[temp_index]:
            distance[temp_index] = dis + temp_dis # "1 -> 탐색중인 노드"의 누적거리를 distance에 저장
            dfs(temp_index,dis + temp_dis) 
if __name__ == "__main__":
    n = int(input())

    if n == 1: # 예외_ n이 1일 경우 ===> 런타임에러
        print(0)
        exit(0) # 정상종료 => 비정상종료 exit(1) : 런타임에러(NZEC)
    
    tree = [[] for _ in range(0,n+1)] # 트리 틀
    tree[0] = -1 # 0번째 인덱스는 더미값
    visited = [False] * (n+1)
    visited[1] = True # 1은 루트노드

    # 1. 임의의 노드 x를 잡는다 : x = 1
    distance = [0] * (n+1) # 1번(루트)노드를 기준으로 각 노드들의 거리
    for i in range(1,n) :
        u,v,d = map(int,input().split())
        tree[u].append([v,d])
        tree[v].append([u,d]) # 노드를 잇는 간선에 가중치를 추가로 담음
    
    # 2. x에서 가장 먼 노드 y를 찾는다
    dfs(1,distance[1])
    node_y = distance.index(max(distance)) # 루트에서 가장 먼 y노드 찾기
    for i in range(0,n+1):
        visited[i] = False
        distance[i] = 0
        # visited와 distance는 node_y로부터 가장 먼 노드를 찾기위해 사용해야하니 초기값으로 초기화

    # 3. y에서 가장 먼 z를 찾는다
    dfs(node_y,0)
    node_z = distance.index(max(distance)) # y노드에서 가장 먼 z노드 찾기
    
    # 4. d(y,z)가 최장거리(지름)
    print(distance[node_z]) # node_y로부터 가장 먼 z노드까지의 거리 출력
    