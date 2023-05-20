# 2606

def dfs(pnode,cnode):
    if visited[cnode] == True:
        return
    visited[cnode] = True
    for next_node in graph[cnode]:
        dfs(cnode,next_node)
    return


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    linked = int(input())
    for _ in range(linked):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    dfs(0,1)

    print(visited.count(True) - 1)