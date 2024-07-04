from collections import deque

def bfs(remove, n, wires):
    queue = deque()
    visited = [False] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    for i in range(len(wires)):
        # 간선 하나 제외
        if i == remove:
            continue
        v1 = wires[i][0]
        v2 = wires[i][1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 1을 시작점으로 bfs 시작
    # 1을 시작으로 연결된 트리와, 연결되지 못한 트리 두 그룹의 개수 차이를 return
    queue.append(1)
    visited[1] = True

    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
    tree_1 = 0
    tree_2 = 0

    for i in range(1, n + 1):
        if visited[i]:
            tree_1 += 1
        else:
            tree_2 += 1

    return abs(tree_1 - tree_2)

def solution(n, wires):
    answer = n + 1

    for i in range(len(wires)):
        answer = min(answer, bfs(i, n, wires))

    return answer

if __name__ == "__main__":
    print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))