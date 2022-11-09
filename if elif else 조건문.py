# if elif else 조건문

###
# if (fruit == 0):
 #   print("과일 못먹음")

#else:
  #  print("과일 먹기")

# ***********************************************************

score = 70

if(score==100):
    print('A+')
elif(score > 70):
    print("B+")
elif(score > 50):
    print("C+")
else:
    print("F")

# *********************************************************

fruit = ["apple","banana","lemon"]

if("apple" in fruit):
    print("사과 있음")
else:
    print("사과 없음")

#**************************************************
a = "apple"
b = "banana"
c = 1
d = 2

if(a=="apple" and b=="banana") :
    print("fruit")