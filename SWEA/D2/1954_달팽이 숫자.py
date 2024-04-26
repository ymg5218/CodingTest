# 오른쪽 -> 아래 -> 왼쪽 -> 위 -> 오른쪽 -> ... 반복

def is_valid(row, col):
    if 0 <= row < N and 0 <= col < N:
        if snail[row][col] == -1:
            return True
        else:
            return False
    else:
        return False

T = int(input())

# 오른쪽, 아래, 왼쪽, 위
d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    N = int(input())

    snail = [[-1 for _ in range(N)] for _ in range(N)]

    forward_idx = 0
    now_row = 0
    now_col = 0
    now_num = 1
    while True:
        if is_valid(now_row, now_col):
            if snail[now_row][now_col] != -1:
                break
        else:
            break

        snail[now_row][now_col] = now_num
        
        now_num += 1
        
        if not is_valid(now_row + d_row[forward_idx], now_col + d_col[forward_idx]):
            forward_idx = (forward_idx + 1) % 4
            
        
        now_row += d_row[forward_idx]
        now_col += d_col[forward_idx]
    print(f'#{test_case}')
    for row in snail:
        for num in row:
            print(num, end=' ')
        print()