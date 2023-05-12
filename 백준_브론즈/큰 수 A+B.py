# 10757

A,B = map(str,input().split())

a = list(A)
b = list(B)
len_a = len(A)
len_b = len(B)
if len_a < len_b:
    for _ in range(len_b - len_a):
        a.insert(0,0)
elif len_a > len_b:
    for _ in range(len_a - len_b):
        b.insert(0,0)

carry = 0
result = []
for i in range(len(a) - 1, -1, -1):
    sum = int(a[i]) + int(b[i])
    if carry == 1:
        sum += 1
        carry = 0

    if sum >= 10:
        sum -= 10
        carry = 1
    
    result.insert(0,sum)

if carry == 1:
    result.insert(0,1)

for i in range(len(result)):
    print(result[i],end="")
