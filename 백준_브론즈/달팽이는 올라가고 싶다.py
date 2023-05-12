# 2869

A,B,V = map(int,input().split())

V -= A

day = V // (A-B)
if V % (A-B) != 0:
    day += 1

print(day + 1)