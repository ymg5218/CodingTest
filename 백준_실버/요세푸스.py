# 1158

N, K = map(int, input().split())

arr = [n + 1 for n in range(N)]
result = []

cur = K - 1
while(N > 0):
    cur %= N
    if arr[cur] == 0:
        cur += 1
        continue

    result.append(arr.pop(cur))
    N -= 1

    cur += K - 1

N = len(result)
print("<", end="")
for i in range(N):
    if i == N - 1:
        print(result[i],end=">")
    else:
        print(result[i],end=", ")