# 1063

if __name__ == "__main__":
    # 방향
    direct = {
        'R' : [0, 1], 'L' : [0, -1], 'B' : [1, 0], 'T' : [-1, 0],
        'RT' : [-1, 1], 'LT' : [-1, -1], 'RB' : [1, 1], 'LB' : [1, -1]
    }

    # A ~ H 까지를 좌표로 변환
    coo = {
        'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7
    }

    coo_reverse = {
        0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H'
    }

    king, stone, N = map(str, input().split())

    # 킹의 좌표 등록
    king_row = abs(int(king[1]) - 8)
    king_col = coo[king[0]]

    # 돌의 좌표 등록
    stone_row = abs(int(stone[1]) - 8)
    stone_col = coo[stone[0]]

    for _ in range(int(N)):
        d = direct[input()]
        d_row = d[0]
        d_col = d[1]
        if 0 <= king_row + d_row < 8 and 0 <= king_col + d_col < 8:
            if king_row + d_row == stone_row and king_col + d_col == stone_col:
                if 0 <= stone_row + d_row < 8 and 0 <= stone_col + d_col < 8:
                    king_row += d_row
                    king_col += d_col
                    stone_row += d_row
                    stone_col += d_col
            else:
                king_row += d_row
                king_col += d_col

    king_row = str(abs(king_row - 8))
    king_col = coo_reverse[king_col]

    print(king_col + king_row)

    stone_row = str(abs(stone_row - 8))
    stone_col = coo_reverse[stone_col]

    print(stone_col + stone_row)
