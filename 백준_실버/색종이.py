# 2563

'''
1. 100x100의 2차원 배열 paper 선언. 각 요소는 0으로 초기화
2. 색종이를 paper에 갖다 댄다고 생각. 해당 색종이가 차지하는 범위를 1로 채움
3. 최종 검은색 색종이가 차지하는 넓이 출력
'''
n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x,y = map(int,input().split())
    for _x in range(x,x + 10):
        for _y in range(y,y + 10):
            if _x >= 100 or _y >= 100:
                break
            paper[_x][_y] = 1
sum = 0
for row in range(100):
    sum += paper[row].count(1)

print(sum)