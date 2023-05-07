# 2566

max_num = -1 # 최댓값을 담을 변수
max_row = 0 # 최댓값의 위치 중, 행 값을 담을 변수
max_col = 0 # 최댓값의 위치 중, 열 값을 담을 변수

# 9개의 행 데이터가 주어짐
for row in range(9):
    # 데이터들을 한 행 씩 받음
    temp_arr = list(map(int,input().split()))
    # 각 행은 9개의 열로 이루어져 있음
    for col in range(9):
        # 입력받은 행 값을 하나씩 검사함
        # 만약 검사중인 값이 최댓값보다 크다면 최댓값, 행 값, 열 값을 갱신 시켜줌.
        if temp_arr[col] > max_num:
            max_row = row + 1
            max_col = col + 1
            max_num = temp_arr[col]

print(max_num)
print("%d %d"%(max_row, max_col))