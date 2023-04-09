# 2562

max = int(input())
max_cnt = 1

cnt = 2
while(cnt < 10):
    a = int(input())
    if max <= a:
        max = a
        max_cnt = cnt
    cnt += 1

print("%d\n%d"%(max,max_cnt))