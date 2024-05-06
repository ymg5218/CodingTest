# 2577

A = int(input())
B = int(input())
C = int(input())

result = A * B * C

str = str(result)

arr = [0 for _ in range(10)]

for i in range(len(str)):
    arr[int(str[i])] += 1

for n in arr:
    print(n)

