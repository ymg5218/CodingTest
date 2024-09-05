# 1325
import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def bfs(start_v):
    cnt = 1

    queue = deque()
    visited[start_v] = True
    queue.append(start_v)

    while queue:
        now_v = queue.popleft()
        for next_v in relation[now_v]:
            if not visited[next_v]:
                visited[next_v] = True
                cnt += 1
                queue.append(next_v)
    return cnt

if __name__ == "__main__":

    N, M = map(int, input().split())
    relation = [[] for _ in range(N + 1)]


    for _ in range(M):
        a, b = map(int, input().split())
        # a가 b를 신뢰하면, b를 해킹했을 때 a 또한 해킹할 수 있음
        relation[b].append(a)

    max_cnt = 1
    result = [0 for _ in range(N + 1)]
    for start_v in range(1, N + 1):
        visited = [False] * (N + 1)
        cnt = bfs(start_v)
        if max_cnt == cnt:
            result.append(start_v)
        elif max_cnt < cnt:
            result.clear()
            max_cnt = cnt
            result.append(start_v)
    print(*result)