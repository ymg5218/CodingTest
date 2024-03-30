# 24479

import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dfs(now_node):
    global visited_order

    if visited[now_node]:
        return
    visited[now_node] = True
    result[now_node] = visited_order
    visited_order += 1
    

    for next_node in graph[now_node]:
        if not visited[next_node]:
            dfs(next_node)

    

if __name__ == "__main__":
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    result = [0 for _ in range(N+1)]
    visited_order = 1

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for linked_list in graph:
        linked_list.sort()
    
    dfs(R)

    for idx in range(1, N + 1):
        print(result[idx])