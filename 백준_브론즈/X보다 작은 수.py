# 10871
N,X = map(int,input().split())

arr = list(map(int,input().split()))
result = []

for i in range(N):
    if arr[i] < X:
        print(arr[i], end=" ")
