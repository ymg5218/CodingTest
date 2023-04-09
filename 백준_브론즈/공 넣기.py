# 10810

N,M = map(int,input().split())

arr = [0] * (N + 1)
cnt = 1
while(cnt <= M):
    start,end,num = map(int,input().split())
    for i in range(start ,end + 1):
        arr[i] = num
    cnt += 1

result = arr[1:]
for i in range(len(result)):
    print(result[i], end= " ")
    