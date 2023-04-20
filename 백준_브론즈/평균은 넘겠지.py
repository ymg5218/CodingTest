# 4344

C = int(input())

for _ in range(C):
    arr = list(map(int,input().split()))
    cnt = arr[0]
    total = 0
    for i in range(1,cnt+1):
        total += arr[i]
    ave = total // cnt

    over = 0
    for i in range(1,cnt+1):
        if ave < arr[i]:
            over += 1
    print("%.3f" %(round((over / cnt) * 100 , 3)),end = "")
    print("%")