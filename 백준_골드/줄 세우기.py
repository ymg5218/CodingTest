# from collections import deque
# import sys
# input = sys.stdin.readline

# def topological_sort(graph, inDegree, N):
#     result = []

#     queue = deque()

#     for i in range(1, N + 1):
#         if inDegree[i] == 0: queue.append(i)
    
#     while queue:
#         now_v = queue.popleft()
#         result.append(now_v)

#         for next_v in graph[now_v]:
#             inDegree[next_v] -= 1
#             if inDegree[next_v] == 0: queue.append(next_v)
    
#     for res in result:
#         print(res, end=" ")

# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     graph = [[] for _ in range(N + 1)]
#     inDegree = [0 for _ in range(N + 1)]
    
#     for _ in range(M):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#         inDegree[v2] += 1
    
#     topological_sort(graph, inDegree, N)

import sys
input = sys.stdin.readline

def topological_sort(graph, inDegree, N):
    result = []

    stack = []

    for i in range(1, N + 1):
        if inDegree[i] == 0: stack.append(i)
    
    while stack:
        now_v = stack.pop()
        result.append(now_v)

        for next_v in graph[now_v]:
            inDegree[next_v] -= 1
            if inDegree[next_v] == 0: stack.append(next_v)
    
    for res in result:
        print(res, end=" ")

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    inDegree = [0 for _ in range(N + 1)]
    
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        inDegree[v2] += 1
    
    topological_sort(graph, inDegree, N)