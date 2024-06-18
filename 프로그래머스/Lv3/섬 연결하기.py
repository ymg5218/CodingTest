def find_parent(x):
    global parents

    # 루트노드 갱신
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    global parents

    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def solution(n ,costs):
    global parents

    answer = 0

    # 비용 기준 오름차순 정렬
    costs.sort(key = lambda x:x[2])

    # 크루스칼로 MST찾기
    # 부모 노드 저장 배열
    parents = [i for i in range(n)]

    for x, y, cost in costs:
        if find_parent(x) != find_parent(y):
            # x, y의 부모노드들 갱신
            union_parent(x, y)

            # x, y 노드와 연결된 모든 노드들의 부모노드 갱신
            union_parent(x, y)

            answer += cost
    return answer


if __name__ == "__main__":
    n = 5
    costs = [[0, 1, 1], [2, 3, 1], [3, 1, 3], [4, 0, 5], [4, 2, 4]]
    print(solution(n, costs))