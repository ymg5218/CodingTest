# 1978

N = int(input())

cnt = 0
arr = list(map(int,input().split()))
for idx in range(N):
    num = arr[idx]
    if num == 1:
        continue
    if num == 2:
        cnt += 1
        continue
    for i in range(2,num):
        if num % i == 0:
            break
        if i >= num // 2 + 1:
            cnt += 1
            break
    
print(cnt)