# 7682

# 0. X와 O의 개수 차이가 2개 이상인 경우 Invalid
# 1. X는 최대 5개, O는 최대 4개
# 2. O가 X보다 많은 경우는 Invalid
# 3. 가로/세로/대각선 중 한 줄이라도 같은 모양으로 채워지면 게임 끝
# -> X, O 둘다 한 줄을 독점하고 있으면 Invalid
# 4. 판이 덜 채워졌는데 아무도 못이겼으면 Invalid
# 5. O가 이겼으면 O,X 개수 같음
# 6. x가 이겼으면 x가 O보다 1개 많음
# 7. 판이 꽉 채워졌는데 아무도 못이겼으면 Valid

def isValid():
    # 3. 둘 다 한 줄씩 독점하고 있는지 가리기 위한 변수
    X_win = 0
    O_win = 0

    # 대각선으로 매칭된 경우
    if game[0][0] == game[1][1] == game[2][2]:
        if game[0][0] == 'X': 
            X_win += 1
        elif game[0][0] == 'O':
            O_win += 1
        
    if game[0][2] == game[1][1] == game[2][0]:
        if game[0][2] == 'X':
            X_win += 1
        elif game[0][2] == 'O':
            O_win += 1
    
    # 가로로 매칭된 경우
    for i in range(0,3):
        if game[i].count('X') == 3:
            X_win += 1
        elif game[i].count('O') == 3:
            O_win += 1
    
    # 세로로 매칭된 경우
    for i in range(0,3):
        if game[0][i] == game[1][i] == game[2][i]:
            if game[0][i] == 'X':
                X_win += 1
            elif game[0][i] == 'O':
                O_win += 1
    
    # 3번 규칙에 의해 Invalid인지 판별
    if (O_win == 1 and X_win == 0) or (O_win == 0 and X_win == 1):
        return "Valid"
    
    # 4. 빈칸이 존재하는데 아무도 못 이긴 경우
    if blank == 0 and O_win + X_win == 0:
        return "Valid"
    # 5. O가 이기고 O,X의 개수가 똑같음
    if (O_win == 1 and X_win == 0) and str.count('O') == str.count('X'):
        return "Valid"
    
    # 6. X가 이기고, O보다 X 개수가 1개 더 많음
    if(O_win == 0 and X_win >= 1) and str.count('O') + 1 == str.count('X'):
        return "Valid"
    if blank > 0 and O_win + X_win == 0:
        return "Invalid"
    
    # 7. 판이 꽉 채워졌는데 아무도 못이겼으니 Valid
    return "Invalid"

if __name__ == '__main__':
    while(1):
        str = input()
        # end 입력받으면 종료
        if str == 'end':
            break
        # 0. O와 X의 개수 차이는 2개 이상이면 Invalid
        # 1. X는 최대 5개, O는 최대 4개
        # 2. O가 X보다 많은 경우는 Invalid
        if str.count('O') > str.count('X') or str.count('O') > 4 or str.count('X') > 5:
            print("Invalid")
        elif abs(str.count('X') - str.count('O')) != 1:
            print("Invalid")
        elif str.count('O') - str.count('X') > 0:
            print("Invalid")
        else:
            blank = str.count('.') # 게임판에 공백 개수 받기
            game = []
            for i in range(0,3):
                game.append([])
                for j in range(0,3):
                    game[i].append(str[3*i+j])

            # 가능한 경우의 수인지 확인
            print(isValid())
                    
        