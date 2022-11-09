<<<<<<< HEAD
<<<<<<< HEAD
# python
# 로또만들기
# 같은 숫자 출력 불가능

import random
num = int(input("로또를 몇 장 구매하시겠습니까? : "))
for n in range(0,num):
    list = [0,0,0,0,0,0]
    for i in range(0,6):
        list[i] = random.randrange(1,45)

    for j in range(0,6):
        for k in range(0,6):
            if(j!=k):
                while(list[j] == list[k]):
                    list[k] = random.randrange(1,45)
        

    print(list)
=======
# python
# 로또만들기
# 같은 숫자 출력 불가능

import random
num = int(input("로또를 몇 장 구매하시겠습니까? : "))
for n in range(0,num):
    list = [0,0,0,0,0,0]
    for i in range(0,6):
        list[i] = random.randrange(1,45)

    for j in range(0,6):
        for k in range(0,6):
            if(j!=k):
                while(list[j] == list[k]):
                    list[k] = random.randrange(1,45)
        

    print(list)
>>>>>>> 7deb61f781ed836e8e4443628b466580998ac552
=======
# python
# 로또만들기
# 같은 숫자 출력 불가능

import random
num = int(input("로또를 몇 장 구매하시겠습니까? : "))
for n in range(0,num):
    list = [0,0,0,0,0,0]
    for i in range(0,6):
        list[i] = random.randrange(1,45)

    for j in range(0,6):
        for k in range(0,6):
            if(j!=k):
                while(list[j] == list[k]):
                    list[k] = random.randrange(1,45)
        

    print(list)
>>>>>>> 7deb61f781ed836e8e4443628b466580998ac552
