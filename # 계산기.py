# 계산기 
name = input("이름을 입력하세요: ") # 이름 받아옴
print("*-"*30 + "*")
print("\t\t%s의 반복계산 프로그램" %name)
print("*-"*30 + "*")
num = int(input("몇 번 반복할까요 ? : "))
while(True): # 계산할때마다 num을 1씩 차감하여 0이되면 종료
    a = float(input("첫번째 정수를 입력하세요 : "))
    b = float(input("두번째 정수를 입력하세요 : "))


    print("%d+%d = %d" %(a,b,a+b)) # 더하기
    print("%d-%d = %d" %(a,b,a-b)) # 빼기
    print("%d*%d = %d" %(a,b,a*b)) # 곱하기
    print("%d/%d = %d" %(a,b,a/b)) # 나누기

    print("%d^%d = %d" %(a,b,a**b)) # a 제곱 b
    print("%d/%d의 나머지 = %d" %(a,b,a%b)) # 나머지연산
    print("%d/%d의 몫 = %d" %(a,b,a//b)) # 몫 연산

    num-=1
    print("남은 계산기 작동 횟수 : %d" %(num))
    if(num<=0):
        break
        

    print("\n")
