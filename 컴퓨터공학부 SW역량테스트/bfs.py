# BFS 너비우선탐색
# LEVEL 순회

from collections import deque


def bfs(graph, start_v):
    q = deque()
    q.append(start_v)
    visited = {start_v : True}

    while q:
        cur_v = q.popleft()
        print(cur_v)
        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append(next_v)
                visited[next_v] = True
        
graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

start_v = 0

bfs(graph, start_v)
# 0 ,1 ,3, 6, 2, 7, 5, 4