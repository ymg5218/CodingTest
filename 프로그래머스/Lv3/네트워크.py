from collections import deque

def solution(n, computers):
    answer = 0

    visited = [False] * n

    for start_v in range(n):
        if visited[start_v]:
            continue
        queue = deque()
        queue.append(start_v)
        visited[start_v] = True

        while queue:
            now_v = queue.popleft()
            for next_v in range(n):
                if next_v == start_v:
                    continue
                if computers[now_v][next_v] == 1 and not visited[next_v]:
                    queue.append(next_v)
                    visited[next_v] = True

        answer += 1

    return answer

if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
