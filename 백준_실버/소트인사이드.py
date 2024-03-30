# 1427

N = input()

arr = []

for i in range(len(N)):
    arr.append(N[i])

arr.sort(reverse=True)

for n in arr:
    print(n, end="")