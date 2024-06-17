def dfs(graph, visited, now_v, sum, visited_cnt):
    global answer

    if len(visited) == visited_cnt:
        answer = min(answer, sum)
        return

    for next_v, cost in graph[now_v]:
        if not visited[next_v]:
            visited[next_v] = True
            dfs(graph, visited, next_v, sum + cost, visited_cnt + 1)
            visited[next_v] = False
            visited_cnt -= 1


def solution(n ,costs):
    global answer
    # n = 100 기준, 간선의 최대 길이 * 간선의 최대 개수 + 1
    INF = ((99 * 100) // 2) ** 2 + 1

    answer = INF

    graph = [[] for _ in range(n)]
    for c in costs:
        graph[c[0]].append([c[1], c[2]])
        graph[c[1]].append([c[0], c[2]])

    for start_v in range(n):
        visited = [False] * n
        visited[start_v] = True
        dfs(graph, visited, start_v, 0, 1)

    return answer


if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))