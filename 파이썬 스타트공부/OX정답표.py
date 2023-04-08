# 채점표를 입력
# O : 1점
# X : 0점
# 대소문자 입력 섞여 있을 수 있다.
# OO 일 경우에는 뒤에 O는 2점처리
# 000일 경우에는 뒤에 O는 3점처리

print("OXquiz 배열")

quiz = input("o,x를 입력하세요 : ")
print(quiz.upper())
quizlist = []
for i in quiz.upper():
    quizlist.append(i) 
num = 0
if(quizlist[0] == 'O'):
    quizlist[0] = 1
else:
    quizlist[0] = 0
for j in range(1,len(quizlist)):
    if(quizlist[j] == 'O'):
        quizlist[j] = quizlist[j-1] + 1
    else:
        quizlist[j] = 0
        
for k in range(0,len(quizlist)):
    num += quizlist[k] 
print(num)