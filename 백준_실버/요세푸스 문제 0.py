# 11866

if __name__ == "__main__":
    N, K = map(int, input().split())

    queue = []

    for i in range(N):
        queue.append(i + 1)

    deleted = 0
    now = 0
    cycle = 1

    result = []
    while deleted < N:
        if queue[now] == -1:
            now += 1
            now %= N
            continue
        
        if cycle == K:
            result.append(queue[now])
            queue[now] = -1
            cycle = 0
            deleted += 1

        now += 1
        now %= N
        cycle += 1
    
    print("<", end="")
    for i in range(N):
        if i == N-1:
            print(result[i],end="")
        else:
            print(result[i],end=", ")
    print(">")
        