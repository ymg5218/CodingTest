# 19532

a, b, c, d, e, f = map(int,input().split())

temp = [a * d, b * d, c * d, d * a, e * a, f * a]

y = (c * d - f * a) // (b * d - e * a)

if a != 0:
    x = (c - (b * y)) // a
else:
    x = (f - (e * y)) // d

print("%d %d" %(x, y))

