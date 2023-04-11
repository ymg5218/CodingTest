# 5597

student = [0 for _ in range(30)]
for _ in range(28):
    check = int(input())
    student[check - 1] = 1

for i in range(0,30):
    if student[i] == 0:
        print(i + 1)


