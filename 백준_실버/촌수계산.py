# 2644
from collections import deque
def bfs(start_v):
    num = 0

    queue = deque()
    next = []
    queue.append(start_v)
    visited[start_v] = True

    while queue:
        next.clear()
        while queue:
            now_v = queue.popleft()
            for next_v in graph[now_v]:
                if not visited[next_v]:
                    if next_v == y:
                        return num + 1
                    next.append(next_v)
                    visited[next_v] = True


        while next:
            queue.append(next.pop())

        num += 1

    return -1


if __name__ == "__main__":
    n = int(input())
    x, y = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    m = int(input())
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(bfs(x))