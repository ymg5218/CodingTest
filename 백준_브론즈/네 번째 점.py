# 3009
import math

x = {}
y = {}
for _ in range(3):
    _x, _y = map(int,input().split())
    if _x in x:
        x[_x] += 1
    else:
        x[_x] = 1
    if _y in y:
        y[_y] += 1
    else:
        y[_y] = 1

result_x = None
result_y = None

result_x = [k for k,v in x.items() if v == 1]
result_y = [k for k,v in y.items() if v == 1]

print(result_x[0], result_y[0])



    


