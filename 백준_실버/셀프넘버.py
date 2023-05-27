# 4673

n = 1
not_selfnum = []
while(n <= 10000):
    _n = str(n)
    temp = n
    for idx in range(len(_n)):
        temp += int(_n[idx])
    if temp <= 10000:
        not_selfnum.append(temp)
    n += 1

not_selfnum.sort()

check_num = 1
while(check_num<= 10000):
    if check_num in not_selfnum:
        not_selfnum.remove(check_num)
    else:
        print(check_num)
    check_num += 1