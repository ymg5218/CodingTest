# 학점 출력
name = input("이름을 입력하세요 : ")
print("---"*9)
print("| \t  %s\t  |"  %name)
print("---"*9)

print("과목 이름 : 수학")
score = int(input("점수 : "))

if(score==100):
    print("%s의 수학 학점 : A+" %name)
elif(score>85):
    print("%s의 수학 학점 : B+" %name)
elif(score>70):
    print("%s의 수학 학점 : C+" %name)    
else:
    print("%s의 수학 학점 : F" %name)
