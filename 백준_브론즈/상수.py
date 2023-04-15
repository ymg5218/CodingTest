# 2908

arr = list(map(str,input().split()))

arr_1 = []
arr_2 = []
for i in range(3):
    arr_1.append(arr[0][i])
    arr_2.append(arr[1][i])
arr_1.reverse()
arr_2.reverse()

num1 = ""; num2 = ""

for i in range(3):
    num1 += arr_1[i]
    num2 += arr_2[i]
 
if int(num1) > int(num2):
    print(num1)
else:
    print(num2)