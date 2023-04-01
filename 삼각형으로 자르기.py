# 1198

# 3개의 좌표가 주어졌을 때, 삼각형의 넓이 : 1/2 * abs((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x3*y2 + x2*y1))
'''
내 예상 풀이
1. 모든 좌표상의 점들을 입력받음.
2. 모든 점 3개를 고르는 경우의 수를 계산해 삼각형의 넓이를 모두 계산함(최악의 경우 : 35 C 3 => 브루트포스 기법)
3. 가장 큰 넓이의 삼각형 출력
'''

N = int(input())

x = [] # x 좌표
y = [] # y 좌표

for _ in range(N):
    temp_x, temp_y = map(int,input().split())
    x.append(temp_x)
    y.append(temp_y)

max_area = -1 # 가장 큰 삼각형 넓이를 담을 max_area 선언

for i in range(N): # x[i], y[i]
    for j in range(i,N): # x[j], y[j]
        for k in range(j,N): # x[k], y[k]
            
            # 3개의 좌표가 주어졌을 때, 삼각형의 넓이 구하는 공식
            area = abs((x[i]*y[j] + x[j]*y[k] + x[k]*y[i]) - (x[i]*y[k] + x[k]*y[j] + x[j]*y[i])) / 2  
            max_area = max(max_area, area)

print(max_area)