#별찍기
name = input("이름을 입력하세요 : ")
print("**"*24 + "*")
print("|\t\t%s의 별찍기\t\t|" %name)
print("**"*24 + "*")
#높이 입력
height = int(input("높이 : "))


#직각삼각형
#for i in range(1,height+1,2): #2씩 증감
#        print("*"*(i))
#print("\n")


#다이아몬드 ( 피라미드 + 1층빠진 역피라미드)
#for i in range(0,height+1): # 0~height 까지
#    print(" "*(height-i)+"*"*(i)+"*"+"*"*(i)+" "*(height-i))
#for j in range(height-1,0): # height-1 부터 0까지
#    print(" "*(height-j)+"*"*(j)+"*"+"*"*(j)+" "*(height-j))


#걍 시험용
#for j in range(height-2,-1,-1):
#  print("*"*(height-j)+" "*(j)+" "+" "*(j)+"*"*(height-j))


#for i in range(height):
#    print("*"*(height-i), end="")
#    print(" "*(i*2+1))
    
#for j in range(height,-1,-1):
#   print(" "*(height-j), end="")
#   print("*"*(j*2+1))

for i in range(height,0,-1): # 반복문은 height부터 1까지 -1씩 가감
    print(" "*(i-1)+"*"*(2*(height-i)+1))

for j in range(i,height+1,+1):# 반복문은 1부터 height까지 +1씩 증감
    print(" "*(j)+"*"*(2*(height-j-1)+1))