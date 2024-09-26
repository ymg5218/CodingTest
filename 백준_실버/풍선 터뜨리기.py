# 2346

def find_nextIdx(next, now_idx):
    if next > 0:
        while next > 0:
            now_idx += 1
            now_idx %= N
            if arr[now_idx] != 0:
                next -= 1

    else:
        while next < 0:
            now_idx -= 1
            if now_idx == -1:
                now_idx = N - 1
            if arr[now_idx] != 0:
                next += 1

    return now_idx

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    now_idx = 0
    # 현재까지 터진 풍선의 개수
    pops = 0
    result = []

    while True:
        result.append(now_idx + 1)

        next = arr[now_idx]
        arr[now_idx] = 0
        pops += 1

        if pops == N:
            break

        now_idx = find_nextIdx(next, now_idx)


    print(*result)


