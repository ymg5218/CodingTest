# 2292

n = int(input())

cnt = 1
start = 1
if n == 1:
    print(1)
    exit()
while(1):
    if n >= start and n <= start + (6 * cnt):
        print(cnt + 1)
        break
    start += 6 * cnt
    cnt += 1