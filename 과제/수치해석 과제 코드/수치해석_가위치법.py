'''
코드 작성 일지 : 2023/03/28

코드 작성자 : 소프트웨어공학과 2017156019 염민규

코드 목적 : 특정 구간에서 주어진 방정식의 해를 "가위치법"을 이용하여 파이썬 코드로 구현하고, 반복 횟수 10회에서의 상대 오차를 비교한다.
'''

import math

# 표 형태로 출력을 깔끔하게 하기 위한 줄 맞춤 틀
titleFormat = '%-10s%-10s%-10s%-9s%-10s\n'
resultFormat = '%-10d%-10.4f%-10.4f%-11.4f%-10.4f\n'


# 표 상단 목록을 먼저 출력
titleOut = titleFormat % ("num","X1","X2","X3(교점)","상대오차(%)")
print(titleOut) # 상단 메뉴 바 출력 => 현재 반복 횟수, X1, X2, 교점 X3, 상대오차

'''
가위치법 함수 : regular_false(start : X1, end : X2, num : 반복 횟수)
최종 목표 : 10번 반복했을 때, 상대 오차를 비교하라
'''
def regular_false(start,end,num):
    if num > 10: # 10번까지만 반복한다.
        return
    
    '''
    점 X1, X2사이에 근이 존재할 때, f(X1)과 f(X2)를 직선으로 연결시켜 이 직선과 x축이 만나는 교점 X3를 새로운 근으로 추정하는 방식
    new_point : X3을 담아낼 변수
    '''
    new_point = end -  f(end) * ((end - start) / (f(end) - f(start)))

    # 반복횟수가 0번째일때는 이전 값 표본이 없기에, 상대오차를 100(%)로 출력하도록 한다.
    if num == 0:
        resultOut = resultFormat % (num,start,end,new_point,100)
        print(resultOut)
    
    # 반복 횟수, X1, X2, X3, 상대오차(%)를 차례대로 출력한다.
    else:
        resultOut = resultFormat % (num,start,end,new_point,abs((new_point - end) / new_point) * 100) 
        # 상대오차 계산에 이용된 end 매개변수는 항상 이전의 반복 계산에서 구했던 근으로 받는다.
        print(resultOut)

    if f(start) * f(new_point) < 0: # start 와 new_point 사이에 근이 존재한다.
        regular_false(start, new_point, num + 1) # 파라미터로 쓰일 점 2개를 start 와 new_point로 채택. 반복 횟수는 1 증가시킨다.

    elif f(new_point) * f(end) < 0: # new_point 와 end 사이에 근이 존재한다.
        regular_false(end, new_point, num + 1) # 파라미터로 쓰일 점 2개를 new_point와 start로 채택. 반복 횟수는 1 증가시킨다.
    
    # 밑의 두 케이스는 적어도 주어진 방정식에선 쓰이지 않는 예외 케이스이다.

    elif f(start) * f(new_point) == 0 or f(new_point) * f(end) == 0: # start, new_point, end 중, 근이 존재한다 
        print("%.5f, %.5f, %.5f 중에 근이 존재합니다." %(start, new_point, end))
        return # 상대오차를 더 비교할 필요가 없기에 재귀를 종료한다.

    else: # 어느 점 사이에도 근이 존재하지 않는 경우
        print("근이 존재하지 않습니다.")
        return # 근이 존재하지 않기에 재귀를 종료한다.


def f(x): # f(x) = x*e**(-x) + 1 = 0
    return x*(math.e ** (-x)) + 1


'''
Q. 구간 [-1,1]에서 다음의 방정식의 해를 "가위치법"을 이용하여 파이썬 코드로 구현하고, 
    반복 횟수 10회에서의 상대 오차를 비교하라.
'''
regular_false(-1, 1, 0) # 초기 파라미터 : -1(start), 1(end), 0(반복 횟수) -> 구간 [-1,1]에서 가위치법을 이용해 상대오차를 비교해보자!
