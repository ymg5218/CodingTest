import sys
sys.setrecursionlimit(10**9) # 최대 재귀호출(10만) 횟수 증가
    # 처음 시도한 함수는 2중for문으로 인한 시간복잡도 n^2으로 시간초과
    # 해결 : 깊이우선탐색 DFS
    # 참고사이트 : https://pythontoomuchinformation.tistory.com/506

def find_pNode(pNode,tree,visited,start):
    visited[start] = True # 탐색한 노드는 True로 지정
    for i in tree[start]: # start번째 노드와 연결된 노드 탐색
        if not visited[i]: # i번째 노드가 start번째 노드의 부모노드가 아니라면
            pNode[i] = start # 현재 start번째 노드는 i번째 노드의 부모노드임
            find_pNode(pNode,tree,visited,i) # i번째 노드의 자식노드가 있는지 재귀호출
        # 만약 탐색한 노드라면? : 위에서 아래로 탐색하는 dfs 특성상 탐색했으면 부모노드임

def main():
    N = int(input()) # 노드 개수 입력받음
    tree = [[]for _ in range(0,N+1)] # 트리 공간 만들기
    visited = [False] * (N+1) # 탐색했는지 확인하기 위한 배열

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a) # 두 노드가 간선으로 연결되었으므로 각 배열에 서로 노드를 남음

    pNode= [-1] * (N + 1) # 각 노드의 부모노드가 무엇인지 담을 배열
    
    find_pNode(pNode,tree,visited,1) # 트리 부모찾기 시작

    for result in range(2,N+1):
        print(pNode[result]) # 2~N번째 노드까지의 모든 부모노드 출력
    

if __name__ == "__main__":
    main()
