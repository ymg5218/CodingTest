# 9063

N = int(input())

max_x = -10001
min_x = 10001
max_y = -10001
min_y = 10001

for _ in range(N):
    x, y = map(int,input().split())
    if max_x < x:
        max_x = x
    if min_x > x:
        min_x = x
    if max_y < y:
        max_y = y
    if min_y > y:
        min_y = y

if max_x == min_x or max_y == min_y:
    print(0)
else:
    print(abs(( max_x - min_x) * (max_y - min_y)))