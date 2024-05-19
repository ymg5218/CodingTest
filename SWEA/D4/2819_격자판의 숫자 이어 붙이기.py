def dfs(now_row, now_col, case):
    if len(case) == 7:
        result.append("".join(case))
        return

    # 동 남 서 북
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    for i in range(4):
        next_row = now_row + d_row[i]
        next_col = now_col + d_col[i]
        if 0 <= next_row < 4 and 0 <= next_col < 4:
            dfs(next_row, next_col, case + [board[next_row][next_col]])


T = int(input())


for t in range(1, T + 1):
    board = []
    for _ in range(4):
        board.append(list(map(str, input().split())))

    result = []

    for row in range(4):
        for col in range(4):
            dfs(row, col, [board[row][col]])

    print(f'#{t} {len(set(result))}')