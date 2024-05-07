# 1167
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**8

def dfs(visited, now_v, length):
    global max_length
    global far_vertex
    if visited[now_v]:
        return
    visited[now_v] = True
    if max_length < length:
        max_length = length
        far_vertex = now_v
    for next_v in graph[now_v]:
        if not visited[next_v[0]]:
            dfs(visited, next_v[0], length + next_v[1])
    

def solution():
    global max_length
    global far_vertex
    max_length = 0
    far_vertex = -1
    # 1번 정점에서 가장 먼 정점 알아내기
    visited = [False] * (V + 1)
    dfs(visited, 1, 0)
    
    max_length = 0
    # 가장 먼 정점에서 가장 먼 정점까지의 거리 = 지름
    visited = [False] * (V + 1)
    dfs(visited, far_vertex, 0)
    
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
            
        