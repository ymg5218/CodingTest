# 10798

arr = [["" for _ in range(15)]for _ in range(5)]

for i in range(5):
    s = input()
    for j in range(len(s)):
        arr[i][j] = s[j]

for col in range(15):
    for row in range(5):
        print(arr[row][col], end= "")