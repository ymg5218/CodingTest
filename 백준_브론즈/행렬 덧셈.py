# 2738

'''
내 예상 풀이
1. 2차원배열 2개를 입력받음
2. 2중for문을 이용해 각 인덱스를 덧셈하여 결과 출력
'''

N,M = map(int,input().split())

arr_1 = []
arr_2 = []

for i in range(N):
    temp = list(map(int,input().split()))
    arr_1.append(temp)

for i in range(N):
    temp = list(map(int,input().split()))
    arr_2.append(temp)
result = [[0 for _ in range(M)] for _ in range(N)]

for row in range(N):
    for col in range(M):
        result[row][col] = arr_1[row][col] + arr_2[row][col]

for i in range(N):
    for j in range(M):
        print(result[i][j],end =" ")
    print()