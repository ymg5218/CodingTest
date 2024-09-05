
if __name__ == "__main__":
    N = int(input())
    find = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]

    now_row, now_col = N // 2, N // 2

    num = 1
    now_go = 0
    go = 1
    turn = 0
    # 북 -> 동 -> 남 -> 서
    forward = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    forward_idx = 0

    '''
    1. 북 -> 동 -> 남 -> 서 방향 순서대로 이동함
    2. 2번째 방향전환(turn)마다 한 번에 갈 수 있는 칸의 개수가 1씩 증가
    3. 
    '''
    while True:
        if turn == 2:
            go += 1
            turn = 0
        board[now_row][now_col] = num

        if go == now_go:
            forward_idx = (forward_idx + 1) % 4
            turn += 1
            now_go = 0

        if now_row == now_col == 0:
            break
        now_row, now_col = now_row + forward[forward_idx][0], now_col + forward[forward_idx][1]
        now_go += 1
        num += 1

    result_row, result_col = 0, 0

    for row in range(N):
        for col in range(N):
            if board[row][col] == find:
                result_row, result_col = row, col
        print(*board[row])

    print(f'{result_row + 1} {result_col + 1}')
