#반복문, 조건문

#while 조건있으면 반복

fruit = 1
while(fruit < 10):
    print(str(fruit) + "번째 사과 먹기")
    fruit+=1
print("반복 끝")

#for

a = [1,2,3,4,5] #리스트(배열)
for i in a : # i가 끝날동안돌린다 = a는 5개니 5번반복
    print(i)

b = ["a","b","c","d","e"]

for j in b :
    print(j)

score = [100,90,80,70,60,50]
for s in score:
    if(s ==100):
        print("A")
    elif(s > 70):
        print("B")
    else :
        print("F")

num = 0
for i in range(0,11): # 0~10까지 i에 대입하라
    print(i)
    num += i

print(num)
