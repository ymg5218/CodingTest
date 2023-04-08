# 윤년계산하기
# 윤년 : if 연도가 4의 배수이면서 100의 배수가 아닐때 elif 또는 400의 배수일 때
name = input("이름을 입력하세요 : ")
print("**"*24 + "*")
print("|\t\t%s의 윤년감별기\t\t|" %name)
print("**"*24 + "*")


year = int(input("연도를 입력하세요 : "))
if(year % 4 == 0 and year % 100 !=0):
    print("윤년입니다.")
elif(year % 400 == 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")