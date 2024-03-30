# 1018

N, M = map(int, input().split())

board = []

color = ["W", "B"]

for _ in range(N):
  board.append(input())

row_end = N - 7
col_end = M - 7

# 가장 많이 색을 칠해도 65 이상 칠할 수 없음
min_cnt = 65

# 원하는 보드 포맷 선언

perfect_board = [
  ["BWBWBWBW",
   "WBWBWBWB",
   "BWBWBWBW",
   "WBWBWBWB",
   "BWBWBWBW",
   "WBWBWBWB",
   "BWBWBWBW",
   "WBWBWBWB"]
   ,
   ["WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
   ]
]

for i in range(2):
  compare_board = perfect_board[i]
  # 시작점 정의
  for start_row in range(row_end):
    for start_col in range(col_end):
      # 부분 보드 탐색 정의
      cnt = 0
      for now_row in range(start_row, start_row + 8):
        for now_col in range(start_col, start_col + 8):
          if board[now_row][now_col] != compare_board[now_row - start_row][now_col - start_col]:
            cnt += 1
      min_cnt = min(min_cnt, cnt)

print(min_cnt)