

T = int(input())

for test_case in range(1, T + 1):
    sum = 0
    N = int(input())
    arr = list(map(int, input().split()))

    # 뒤에서부터 비교할 것
    now_idx = N - 1
    compair_idx = now_idx - 1
    while compair_idx >= 0:
        if arr[now_idx] < arr[compair_idx]:
            now_idx = compair_idx
            compair_idx -= 1
        else:
            sum += (arr[now_idx] - arr[compair_idx])
            compair_idx -= 1
        

    print(f'#{test_case} {sum}')