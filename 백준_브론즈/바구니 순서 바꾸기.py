# 10812

N,M = map(int,input().split())

basket = [i for i in range(N+1)]

for _ in range(M):
    start,end,mid = map(int,input().split())
    temp = basket[start:end+1]
    for idx in range(len(temp)):
        basket[idx + start] = temp[(mid - start + idx) % len(temp)]
result = basket[1:]
for x in result:
    print(x,end=" ")