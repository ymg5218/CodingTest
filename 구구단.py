# 몇단을 출력할 것인지 입력받기
# for문으로 출력
name = input("이름을 입력하세요 : ")
print("**"*24 + "*")
print("|\t\t%s의 구구단\t\t\t|" %name)
print("**"*24 + "*")
print("\n")

#num = int(input("몇 단의 곱셈을 출력할까요? : "))
for j in range(1,10):
    print(" ********** %d단 **********" %j)
    for i in range(1,10):
        print("%d * %d = %d" %(j,i,j*i))

    print("\n")
