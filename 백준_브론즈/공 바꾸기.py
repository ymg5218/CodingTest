# 10813

N,M = map(int,input().split())

arr = [i for i in range(0,N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    swap_a = arr[a]
    swap_b = arr[b]

    arr[a] = swap_b
    arr[b] = swap_a

result = arr[1:]
for idx in range(N):
    print(result[idx], end=" ")