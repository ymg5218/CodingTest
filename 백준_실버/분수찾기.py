# 1193

x = int(input())
n = 0
cnt = 0

while(n < x):
    cnt += 1
    n += cnt

gap = abs(n - x)

if cnt % 2 != 0:
    start = 1 + gap
    end = cnt - gap
    print("%d/%d"%(start,end))
else:
    start = cnt - gap
    end = 1 + gap
    print("%d/%d"%(start,end))


