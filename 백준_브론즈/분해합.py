# 2231

N = int(input())

now = 0
while True:
    if now > N:
        print(0)
        break

    sum = now
    str_now = str(now)
    for idx in range(len(str_now)):
        sum += int(str_now[idx])
    
    if sum == N:
        print(now)
        break
    

    now += 1