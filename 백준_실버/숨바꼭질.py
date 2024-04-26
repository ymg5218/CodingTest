# 1697

from collections import deque

def bfs(N):
    queue = deque([])
    next_queue = deque([])
    queue.append(N)

    while True:
        while queue:
            now_point = queue.popleft()
            if now_point == K:
                return visited[now_point]
            
            for next_point in (now_point - 1, now_point + 1, now_point * 2):
                if 0 <= next_point <= 100000 and not visited[next_point]:
                    next_queue.append(next_point)
                    visited[next_point] = visited[now_point] + 1

        
        while next_queue:
            now_point = next_queue.popleft()
            queue.append(now_point)



if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [0] * 100001
    print(bfs(N))
               