# 17608
import sys
input = sys.stdin.readline

N = int(input())
stack = []
stack.append(int(input()))
length = 1

for _ in range(N - 1):
    next = int(input())
    while stack and next >= stack[-1]:
        stack.pop()
        length -= 1
    stack.append(next)
    length += 1

print(length)