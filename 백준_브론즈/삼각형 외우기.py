# 10101

angle = []
total = 0
angle_60 = 0
for _ in range(3):
    _a = int(input())
    angle.append(_a)
    total += _a
    if _a == 60:
        angle_60 += 1

if total == 180:
    if angle_60 == 3:
        print("Equilateral")
        exit()
    isIso = False
    for i in range(3):
        for j in range(i+1, 3):
            if angle[i] == angle[j]:
                isIso = True
                break
    if isIso == True:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")


    
