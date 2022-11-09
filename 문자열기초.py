# #은 주석
# ''' 은 여러줄 주석
'''
a = float(input("a를 입력하세요 : "))
b = float(input("b를 입력하세요 : "))


print(a+b) # 더하기
print(a-b) # 빼기
print(a*b) # 곱하기
print(a/b) # 나누기

print(a**b) # a 제곱 b
print(a%b) # 나머지연산
print(a//b) # 몫 연산
'''

a = "Hello World"
b = "10"
# c = "가나다라마바사\t아자차카타파하"
print(a+b)

print("*-"*30+"*")

d = "                "
print(len(d))

e = "APPLE"
print(e[2])

#문자열 인덱싱
f = "ABCDEFG"
print(f[1:3]) # 1에서 3 전까지 출력
print(f[1:]) # 1부터 출력
print(f[:4]) # 4 전까지 출력

#정수 삽입
g = 3
print("I ate %d apples" %(g))

print("a의 첫번째 문자열은 %c 이다" %a[0])

# 문자 개수 검색
a.count('l')