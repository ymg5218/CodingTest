# 3052

arr = []
for _ in range(10):
    n = int(input())
    arr.append(n % 42)

print(len(list(set(arr))))