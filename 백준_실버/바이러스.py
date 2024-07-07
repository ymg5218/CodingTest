# 2606

def dfs(now_node):
    if visited[now_node] == True:
        return
    visited[now_node] = True
    for next_node in graph[now_node]:
        dfs(next_node)
    return


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    
    # 간선의 개수
    linked = int(input())
    
    for _ in range(linked):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    dfs(1)
    
    # 1번 컴퓨터를 제외한 네트워크에 포함된 컴퓨터 개수 출력
    print(visited.count(True) - 1)