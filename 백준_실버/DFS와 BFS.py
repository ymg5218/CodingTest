# 1260

import sys
from collections import deque

input = sys.stdin.readline

def dfs(now):
    if visited_DFS[now] == True:
        return
    visited_DFS[now] = True
    result_DFS.append(now)
    for next in graph[now]:
        if visited_DFS[next] == False:
            dfs(next)
            

def bfs(now):
    queue.append(now)
    visited_BFS[now] = True
    while len(queue) > 0:
        pop_node = queue.popleft()
        result_BFS.append(pop_node)
        for next in graph[pop_node]:
            if visited_BFS[next] == False:
                queue.append(next)
                visited_BFS[next] = True
        
    

if __name__ == "__main__":
    N, M, V = map(int, input().split())
    
    # N + 1 크기의 graph 리스트로 선언
    graph = [[] for _ in range(N + 1)]
    # 0번째 인덱스는 더미값 -1 삽입
    graph[0].append(-1)

    # 인접리스트 형태로 그래프 세팅
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것부터 방문하기 위함
    for idx in range(N + 1):
        graph[idx].sort()
    
    # 깊이 우선 탐색
    visited_DFS = [False] * (N + 1)
    result_DFS = []
    dfs(V)
    for v_dfs in result_DFS:
        print(v_dfs, end=" ")
    print()

    # 너비 우선 탐색
    visited_BFS = [False] * (N + 1)
    queue = deque()
    result_BFS = []
    bfs(V)
    for v_bfs in result_BFS:
        print(v_bfs, end=" ")