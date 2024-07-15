# 10971번
import sys
input = sys.stdin.readline

def dfs(now_v, visitedCnt, nowDis):
    global minResult
    if visitedCnt == N:
        if city[now_v][0] != 0:
            minResult = min(minResult, nowDis + city[now_v][0])
        return

    for idx in range(N):
        next_v = city[now_v][idx]
        if not visited[idx] and next_v != 0:
            visited[idx] = True
            dfs(idx, visitedCnt + 1, nowDis + next_v)
            visited[idx] = False


if __name__ == "__main__":
    N = int(input())
    city = []
    visited = [False] * N
    visited[0] = True
    for _ in range(N):
        city.append(list(map(int, input().split())))

    minResult = 10**6 * 10 + 1

    dfs(0, 1, 0)

    print(minResult)
