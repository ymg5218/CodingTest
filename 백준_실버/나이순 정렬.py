# 10814

N = int(input())

order = 0
arr = []

for _ in range(N): 
    age, name = map(str, input().split())
    arr.append([age, name, order])
    order += 1

arr.sort(key=lambda x : (int(x[0]), x[2]))

for info in arr:
    print(info[0], info[1])