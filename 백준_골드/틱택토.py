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

def flag(arr,equ):
    #print(arr,equ)
    if arr[0][0]==arr[0][1]==arr[0][2]==equ:
        return True
    if arr[1][0]==arr[1][1]==arr[1][2]==equ:
        return True
    if arr[2][0]==arr[2][1]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][0]==arr[2][0]==equ:
        return True
    if arr[0][1]==arr[1][1]==arr[2][1]==equ:
        return True
    if arr[0][2]==arr[1][2]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][1]==arr[2][2]==equ:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==equ:
        return True
    return False
    

while True:
    string=input()
    if string=="end":
        break
    else:
        xcnt=0
        ocnt=0
        index=0
        arr=[[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                arr[i][j]=string[index]
                if string[index]=="X":
                    xcnt+=1
                if string[index]=="O":
                    ocnt+=1
                index+=1
        if xcnt>ocnt+1:
            print("invalid")
            continue
        if ocnt>xcnt:
            print("invalid")
            continue
        if ocnt==xcnt:
            if flag(arr,"O") and not flag(arr,"X"):
                print("valid")
                continue
        if ocnt+1==xcnt:
            if flag(arr,"X") and not flag(arr,"O"):
                print("valid")
                continue
        if xcnt==5 and ocnt==4:
            if not flag(arr,"O"):
                print("valid")
                continue
        print("invalid")