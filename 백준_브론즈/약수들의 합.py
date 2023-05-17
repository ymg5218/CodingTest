# 9506

while(1):
    n = int(input())
    if n == -1:
        break
    sum = 0
    result = []
    for i in range(1,n):
        if n % i == 0:
            sum += i
            result.append(i)
    
    if sum != n:
        print("%d is NOT perfect."%n)
    else:
        print("%d ="%n,end = " ")
        for idx in range(len(result)):
            if idx == len(result) - 1:
                print(result[-1])
            else:
                print("%d +"%result[idx],end = " ")
            