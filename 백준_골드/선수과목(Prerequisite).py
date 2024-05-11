# 14567

# # dfs 시간복잡도 : N^2 * M ~= 5 * 10**12 -> 시간 초과 우려
import sys
input = sys.stdin.readline

# def dfs(now_v, seq):
#     if visited[now_v]:
#         return
#     visited[now_v] = True
    
#     result[now_v] = max(result[now_v] , seq)

#     for next_v in graph[now_v]:
#         if not visited[next_v]:
#             dfs(next_v, seq + 1)
#             visited[next_v] = False

def solution():
    for idx in range(N + 1):
        arr = object[idx]
        for pre_obj in arr:
            dp[idx] = max(dp[idx], dp[pre_obj] + 1)

    
    for re in range(1, N + 1):
        print(dp[re], end= " ")

if __name__ == "__main__":
    N, M = map(int, input().split())

    object = [[] for _ in range(N + 1)]
    for _ in range(M):
        pre, later = map(int, input().split())
        object[later].append(pre)

    # graph = [[] for _ in range(N + 1)]
    
    # for _ in range(M):
    #     v1, v2 = map(int, input().split())

    #     graph[v1].append(v2)
    
    # visited = [False] * (N + 1)
    
    # result = [-1 for _ in range(N + 1)]
    # for i in range(1, N + 1):
    #     dfs(i, 1)
    
    # for idx in range(1, N + 1):
    #     if result[idx] == -1:
    #         print(1, end=" ")
    #     else:
    #         print(result[idx], end=" ")

    dp = [ 1 for _ in range(N + 1)]

    solution()

