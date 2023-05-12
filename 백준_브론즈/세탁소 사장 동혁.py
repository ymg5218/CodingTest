# 2720

T = int(input())

change = [25,10,5,1]
for _ in range(T):
    money = int(input())
    for i in range(4):
        print(money // change[i], end = " ")
        money %= change[i]
    print()