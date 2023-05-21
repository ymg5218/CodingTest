# 11653

N = int(input())

if N == 1:
    exit()
result = []
cnt = 2
while(1):
    if cnt >= N:
        result.append(cnt)
        break
    if N % cnt == 0:
        result.append(cnt)
        N //= cnt
    else:
        cnt += 1
for i in range(len(result)):
    print(result[i])
    