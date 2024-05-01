# 1167
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**8

def dfs(visited, now_v, length):
    global max_length
    if visited[now_v]:
        return
    visited[now_v] = True
    max_length = max(max_length, length)
    for next_v in graph[now_v]:
        if not visited[next_v[0]]:
            dfs(visited, next_v[0], length + next_v[1])
    

def solution():
    global max_length
    max_length = 0
    for i in range(1, V + 1):
        visited = [False] * (V + 1)
        dfs(visited, i, 0)
    
    print(max_length)

if __name__ == "__main__":
    V = int(input())

    graph = [[] for _ in range(V+1)]
    
    for _ in range(V):
        arr = list(map(int, input().split()))[:-1]
        v = arr[0]
        e_infos = arr[1:]
        
        for idx in range(len(e_infos)):
            if idx % 2 == 0:
                e_info = []
                e_info.append(e_infos[idx])
            else:
                e_info.append(e_infos[idx])
                graph[v].append(e_info)
    
    solution()
            
        