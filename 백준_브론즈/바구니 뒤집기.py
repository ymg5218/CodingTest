# 10811

N,M = map(int,input().split())

arr = [i for i in range(N+1)] # 0번째 인덱스는 더미값

for _ in range(M):
    start,end = map(int,input().split())
    temp = arr[start:end+1]
    temp.reverse()
    for i in range(len(temp)):
        arr[start + i] = temp[i]

for idx in range(1,N+1):
    print(arr[idx], end = " ")