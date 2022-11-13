# 15681

# 트리 노드의 수 : N
# 루트 번호 : R
# 쿼리의 수 : Q
# 노드 U를 루트로 하는 서브트리에 속한 노드의 개수 출력하기
#       1
#   2       3
# 4   5   6   7
# 2를 루트로 하는 서브트리에 속한 노드의 개수 : 3개
# 5를 루트로 하는 서브트리에 속한 노드의 개수 : 1개
# 깊이우선탐색을 활용해서 각 노드의 자식노드들의 개수를 모두 더하면 되지 않을까
# 참고 : 15681 하단 힌트

import sys
input = sys.stdin.readline # 입력시간 단축시켜봄
sys.setrecursionlimit(10**9) # 최대 재귀호출 횟수 증가

# 트리의 부모 찾기에서 쓴 dfs 재활용
def query_dfs(start): # 깊이우선탐색을 이용하여 각 노드의 자식노드 개수 찾아내기
    countNode[start] = 1 # 자기 자신 카운트에 추가
    visited[start] = True # 방문했으니 True
    for node in tree[start]: # start번째 노드와 연결된 node들 탐색
        if not visited[node]: # 탐색하지 않은 노드 : 자식노드
            query_dfs(node) # 자식노드들 탐색 - 재귀호출
            countNode[start] += countNode[node] # 자식노드가 더 없으면 부모노드에 합산하는 식
    

if __name__ == "__main__":
    N, R, Q = map(int, input().split())
    tree = [[]for _ in range(0,N+1)] # 트리 공간 만들기
    visited = [False] * (N+1) # 탐색했는지 확인하기 위한 배열
    pNode = [-1] * (N+1) # 부모자식관계 담아낼 배열
    
    for _ in range(N-1): # U V는 하나의 간선에 연결된 노드들
        U, V = map(int, input().split())
        tree[U].append(V)
        tree[V].append(U) # 두 노드가 간선으로 연결되었으므로 각 배열에 서로 노드를 남음

    nodeU = [] # 개수를 찾아낼 서브트리들의 루트값 저장
    for i in range(0,Q):
        temp = int(input())
        nodeU.append(temp)

    countNode = [0] * (N+1) # 각 노드의 자식노드 개수 담을 배열.
    query_dfs(R) # 루트노드를 시작으로 모든 노드 탐색

    for i in nodeU:
        print(countNode[i])