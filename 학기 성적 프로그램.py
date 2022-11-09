# 학기 성적 프로그램

name = input("이름을 입력하세요 : ")
print("**"*24 + "*")
print("|\t   %s의 학기 성적표\t\t|" %name)
print("**"*24 + "*")
print("\n")


subject = ["국어","수학","사회","과학"] # subject라는 과목 배열 선언
print("\n")

print("<%s의 이번학기 성적표 >" %(name))
for i in range(0,4):
    score = int(input("%s 점수 : " %(subject[i])))

    if(score == 100):
        print("%s 과목 학점 : A+" %(subject[i]))
    elif(score > 95):
        print("%s 과목 학점 : A" %(subject[i]))
    elif(score > 70):
        print("%s 과목 학점 : B" %(subject[i]))
    elif(score > 55):
        print("%s 과목 학점 : C" %(subject[i]))
    else:
        print("%s 과목 학점 : F" %(subject[i]))  
