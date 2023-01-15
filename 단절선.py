#11400

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, parent):
    global cnt
    cnt += 1
    visited[start] = True # 방문한 노드는 True로 분류
    order[start] = cnt # 방문 순서 기입
    lsv = order[start] # 주변 최소 순번 변수 lsv

    for childNode in graph[start] : # 해당 노드와 연결된 자식노드들 탐색
        if childNode == parent : # 부모노드로 돌아가는 것은 무시한다
            continue
        
        if visited[childNode] == True : # 이미 방문한 상태라면
            lsv = min(lsv, order[childNode]) # 방문했던 노드를 주변 최소 순번으로 설정하고 진행
            continue
        
        subtree = dfs(childNode, start) # 서브트리도 dfs 탐색
        lsv = min(subtree, lsv) # 주변 최소 순번이 서브트리의 부모 노드와 주변 최소 순번 노드 중, 작은 값으로 설정

        # 현재 간선을 제외하고 우회로가 없다면 : 브릿지
        """판별 방법"""
        # 서브트리의 dfs 반환 값(주변 최소 순번)이 부모 노드의 순번보다 크다 : 브릿지
        if subtree > order[start] :
            bridge.append((start,childNode))
    
    return lsv # 주변 최소 순번을 return


if __name__ == "__main__":
    V,E = map(int, input().split())

    graph = [[]for _ in range(0,V+1)] # 그래프 틀 선언
    # 크기가 노드의 개수 + 1인 이유 : 0번째 인덱스는 더미로 둘 것이기 때문.

    visited = [False] * (V+1) # dfs를 위한 방문여부 확인 bool 리스트
    # 크기가 노드의 개수 + 1인 이유 : 0번째 인덱스는 더미로 둘 것이기 때문.

    order = [-1] * (V+1) # 순회를 체크하기 위한 배열 선언. -1로 초기화
    # 크기가 노드의 개수 + 1인 이유 : 0번째 인덱스는 더미로 둘 것이기 때문.


    for i in range(0,E):
        v1, v2 = map(int,input().split())
        # 그래프에 각 노드의 연결성 삽입
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    #graph를 출력하면 인접리스트의 형태로 저장되었음을 알 수 있다.
    
    bridge = [] # 브릿지를 담을 배열 선언

    cnt = 0 # 노드 방문 순서를 나타내는 변수
    
    dfs(1, None)
    
    # 모든 간선의 양 끝점은 [작은수 노드, 큰 수 노드] 로 통일시키기 위해 정렬을 진행
    # 이는 간선의 양 끝점을 입력받아 브릿지 여부 판단할 때, 데이터의 정렬을 통일시켜 브릿지인지 판단하기 용이하기 위함.
    
    bridge.sort()
    print(len(bridge))
    for x,y in bridge:
        print(x,y)
    
