# 1005
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    queue = deque()
    for idx in range(1, N + 1):
        if inDegree[idx] == 0:
            queue.append(idx)
            build_time[idx] = time[idx]
    
    while queue:
        now = queue.popleft()
        for next in build[now]:
            inDegree[next] -= 1
            build_time[next] = max(build_time[next], build_time[now] + time[next])
            if inDegree[next] == 0:
                queue.append(next)
    
    return build_time[W]

if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        N, K = map(int, input().split())

        build = [[] for _ in range(N + 1)]

        build_time = [0] * (N + 1)

        inDegree = [0 for _ in range(N + 1)]

        time = [0] + list(map(int, input().split()))
        for _ in range(K):
            v1, v2 = map(int, input().split())
            build[v1].append(v2)
            inDegree[v2] += 1
        
        W = int(input())
    
        print(solution())