# 프로그램 제목 출력
# 메뉴판 출력
# 입금한 돈 구매품목,구매수량을 입력받을 때, 가이드 텍스트 출력하기
# 주문한 금액이 입금한 금액보다 많으면 예외처리
# 주문한 금액을 빼고 거스름돈을 돌려준다. ( 5000, 1000, 500, 100)
# 문자열 포매팅 사용

#재고량 + 구매수량 추가
name = input("이름을 입력하세요 : ")
print("**"*24 + "*")
print(" \t   %s의 E동 5층의 자판기\t\t" % name)
drink = [["1. 콜라 : 1000원",1000,10], ["이트 : 602. 스프라0원",600,10], ["3. 오렌지주스 : 500원",500,10], ["4. 코코팜화이트 : 700원",700,10],
         ["5. 토레타 : 1300원",1300,10], ["6. 코코팜 : 700원",700,10], ["7. 식혜 : 600원",600,10], ["8. 유자차 : 600원",600,10]]
    

print("**"*24 + "*")
print("\n")

won = [["5000원",0],["1000원",0],["500원",0],["100원",0]]

# ***************************************************************
def menu(): # 메뉴판 출력
    print("**"*24 + "*")
    print(" \t   %s의 E동 5층의 자판기\t\t" % name)
    for i in range(0, len(drink)):
        print("%s || 재고량 : %d 개" % (drink[i][0],drink[i][2]))
    print("**"*24 + "*")
    
    print("\n")

def selectnum(): # 선택지
    selectnum = int(input("상품을 주문하려면 ' 1 ', 잔돈을 출력하려면 ' 2 '를 입력하세요 : "))
    return selectnum

def drinkout(sub): # 음료출력함수
    while(True):
        menu() # 메뉴판 함수 출력
        select = selectnum() # selectnum을 return받아 select에 삽입
        if(select==1):
            # 상품 번호 입력받기
            num = int(input("주문할 상품의 번호를 입력해주세요! : "))
            #예외처리 2 ) 재고량 부족
            if(drink[num-1][2] == 0): 
                print("error : 재고량이 부족합니다.")
                continue
            count = int(input("주문할 상품의 개수를 입력하세요 : "))
            #예외처리 3 ) 입력개수가 현재 재고량보다 많은 경우
            if(drink[num-1][2] < count):
                print("error : 재고량이 부족합니다.")
                continue
            #예외처리 4 ) 음료개수를 0개 이하로 입력한 경우
            elif(count <=0):
                print("error : 1개 이상의 음료를 입력하세요.")
                continue
            #예외처리 5 ) 현재 돈 - 음료가격이 0보다 작은 경우
            if((sub - (drink[num-1][1])*count )< 0): 
                print("error : 돈이 부족합니다.")  # 에러문구 출력
                continue  # 실행즉시종료
            # sub 변수에 현재 돈 - 음료가격 값 저장
            sub = sub - (drink[num-1][1])*count 
            drink[num-1][2]-=count # 개수 차감
            print("남은 금액은 %d 입니다." % sub)
            # 돈 입력액수 - 상품의 가격
        else:
            return sub
        

def change(sub):
    while(sub > 0):
        if(sub // 5000 != 0):
            won[0][1] += sub/5000  # 5천원 개수 출력
            sub = sub % 5000
        elif(sub // 1000 != 0):
            won[1][1] += sub/1000  # 1천원 개수 출력
            sub = sub % 1000
        elif(sub // 500 != 0):
            won[2][1] += sub/500  # 5백원 개수 출력
            sub = sub % 500
        else:
            won[3][1] += sub/100  # 1백원 개수 출력
            sub = sub % 100
    #for문으로 잔돈출력
    for k in range(0,4):
        print("%s : %d 장" %(won[k][0],won[k][1]))
# *****************************************************************

# 돈 입력받기
sub = int(input("돈을 투입구에 투입해주세요 : "))
#예외처리 1 ) 100원미만의 금액 받지않기
if(sub%100 != 0):
    print("100원 미만의 금액단위는 받지 않습니다.")
    print("%d원 출력" %sub)
    exit(1)
#drinkout(sub) # 음료출력함수
sub = drinkout(sub)
    
    

#잔돈계산하자
change(sub) # 잔돈 계산 함수




