# 1874
import sys
input = sys.stdin.readline

n = int(input())
stack = []
arr = []
for _ in range(n):
    arr.append(int(input()))

cur = 1
now = 0

result = []
while(cur <= n + 1 and now < n):
    if stack and stack[-1] == arr[now]:
        stack.pop()
        now += 1
        result.append("-")
    else:
        stack.append(cur)
        cur += 1
        result.append("+")

if stack:
    print("NO")
else:
    for op in result:
        print(op)


    

