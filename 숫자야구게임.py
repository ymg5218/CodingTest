import random
def randbase(): # 랜덤수 선택 함수
    base = [-1, -1, -1]  # 랜덤수를 삽입할 base 배열 선언
    for i in range(0, 3):
        base[i] = random.randrange(0, 10)
        for j in range(0, 3):
            if(i != j):
                if(base[i] == base[j]):
                    base[i] = random.randrange(0, 10)
    return base # base 배열 리턴

#num = 0  # 시도횟수 num은 1로 시작
def game(num,base): # 게임 프로그램 함수
    while(num < 9):
        num+=1
        strike = 0
        ball = 0  # strike와 ball 변수는 0으로 지정. 초기화
        userbase = [-1, -1, -1]  # 입력한 숫자를 집어넣을 배열 초기화
        print("중복이 없게 세 자리를 차례로 입력하세요")
        print("%d 번째 도전" %num)
        for j in range(0, 3):
            try:
                userbase[j] = int(input("%d번째 숫자를 입력하세요 ( 0~9 ) : " % (j+1)))
                for k in range(0, 3):
                    if(j != k):
                        if(userbase[j] == userbase[k]):
                            userbase[j] = int(input("%d번째 숫자를 입력하세요 ( 0~9 ) : " % (j+1)))
            except ValueError: # 문자입력오류
                print("{}는 숫자가 아닙니다. 숫자를 입력해주세요." .format(userbase[j]))
            else:
                if(userbase[j]<0 or userbase[j]>9):
                    print("0~9 사이의 숫자만 입력해주세요.")
                    
                else:
                    pass # 통과
        isout = True # out을 print 할지 안할지 결정 기준값
        for i in range(0, 3):
            if(base[i] == userbase[i]):
                strike += 1  # 숫자와 자릿수까지 일치하면 strike 1 증가
                isout = False
            elif(userbase[i] in base):
                ball += 1  # 숫자는 같은게 존재한다면 ball 1 증가
                isout = False
        if(isout == True):
            print("out")
            continue
        
        print("%d 스트라이크 , %d 볼 \n" % (strike, ball))  # 스트라이크, 볼 출력
        
        if(strike >= 3):  # 스트라이크가 3이 나온다면
            print("승리!")
            print("%d 번" %num)
            exit(1)  # 승리 출력 후 종료



    
def gameover(base):
    print("패배")  # 9번의 시도 동안 맞추지 못한다면 패배 출력 및 종료
    print("정답 : %d%d%d" %(base[0],base[1],base[2]))
#*********************************************************


base = randbase() # base 배열을 매개변수로 받기 위함
game(0,base) # 게임 프로그램 함수. 
#num은 0으로 디폴트값을 가짐. base 배열을 매개변수로 들여옴
gameover(base) # base 배열을 매개변수로 가져옴. 정답을 출력하기 위함.

