from collections import deque

def solution(n, edge):
    answer = 0
    INF = 50001

    graph = [[] for _ in range(n + 1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    distance = [INF for _ in range(n + 1)]

    # 다익스트라
    queue = deque()
    queue.append(1)
    distance[1] = 0

    while queue:
        # 현재 도착한 노드
        now_v = queue.popleft()
        # 갈 수 있는 연결된 노드 탐색
        for next_v in graph[now_v]:
            # 갈 수 있는 연결된 노드로 가는 누적 거리 계산
            next_dis = distance[now_v] + 1
            # 누적 거리가, 지금까지 해당 노드로 갈 수 있는 거리보다 짧다면 갱신
            if distance[next_v] > next_dis:
                distance[next_v] = next_dis
                # 해당 노드 방문예정 처리
                queue.append(next_v)

    distance.sort(reverse=True)

    # 거리가 가장 먼 노드 개수 파악하기
    # 0번째 인덱스는 더미 인덱스이고 값은 무조건 최대값이기에 내림차순 정렬 후 0번째 인덱스는 고려하면 안됨.
    longest = distance[1]
    answer += 1
    for idx in range(2, n):
        if longest == distance[idx]:
            answer += 1
        else:
            break

    return answer


if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

    print(solution(n, edge))