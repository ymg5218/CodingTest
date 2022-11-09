# 등수 알아내기
name = input("이름을 입력하세요: ")
print("---"*9)
print("| \t  %s\t  |"  %name)
print("---"*9)

score = int(input("당신의 점수를 입력하세요: "))
list = [20,40,50,30,10,70,80,90] # 배열 선언

list.append(score) # 내 점수를 배열에 추가

list.sort() # 배열 정렬
list.reverse() # 배열 반대로 순서뒤집기

#list.index(score) 
print(list)
print("%s의 등수는 %d등 입니다." %(name,list.index(score)+1))