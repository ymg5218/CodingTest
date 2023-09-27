# 2798

N, M = map(int, input().split())

arr = list(map(int, input().split()))
max_num = 0
for idx_1 in range(N):
    for idx_2 in range(idx_1 + 1, N):
        for idx_3 in range(idx_2 + 1, N):
            temp = arr[idx_1] + arr[idx_2] + arr[idx_3]
            if temp == M:
                print(temp)
                exit()
            if temp < M and M - temp < M - max_num:
                max_num = temp

print(max_num)