# 수치해석 과제02 - 8번 문제 풀이용 코드
'''
코드 작성 일지 : 2023/05/08

코드 작성자 : 소프트웨어공학과 2017156019 염민규

코드 목적 : 3차 스플라인 보간법을 이용해 구간 내 특정 값을 근사한다.
'''

import numpy as np

def f(xi):
    if xi == 40:
        return 1.36
    elif xi == 48:
        return 1.67
    elif xi == 56:
        return 2.12
    elif xi == 64:
        return 2.36
    elif xi == 72:
        return 2.72
    elif xi == 80:
        return 3.19
    else:
        print("입력 xi값 확인 바람")
        return
    
def _f(x1,x2):
    return (f(x2) - f(x1)) / (x2 - x1)

def getC(A,B):
    _A = np.linalg.inv(A) # _A : A의 역행렬

    C = np.dot(_A,B.T)# 계수 C는 _A 와 B의 전치행렬의 곱연산
    return C

def ai(i):
    global X
    return f(X[i])

def bi(a1,a2,c1,c2):
    # 모든 xi+1 - xi 는 8임.
    return (1 / 8) * (a2 - a1) - (8 / 3) * (c2 + 2*c1)


def ci(i):
    global c
    return c[i-1]

def di(i,x1,x2):
    return (ci(i+1) - ci(i)) / 3 * (x2 - x1)


# 범위가 포함되는 x5~x6 : 72~80 범위에서의 3차 스플라인을 구하기 위해 s5(x)만 선언하였음
def s5(x):
    global a,b,c,d
    global X
    return a[4] + ( b[4] * (x - X[4]) ) + ( c[4] * (x - X[4])**2 ) + ( d[4] * (x - X[4])**3 )

if __name__ == "__main__":

    X = [40, 48, 56, 64, 72, 80]
    Y = [1.36, 1.67, 2.12, 2.36, 2.72, 3.19]

    A = np.array([[1,0,0,0,0,0], [8,32,8,0,0,0],[0,8,32,8,0,0],
                [0,0,8,32,8,0], [0,0,0,8,32,8],[0,0,0,0,0,1]])
    B = np.array([0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 ])
    
    # A * C = B
    # C를 구하기 위해 A-1 * B를 진행할 것.
    # B 구하기
    for i in range(0,4):
        result = 3 * ( _f(X[i+2],X[i+1]) - _f(X[i+1],X[i]))
        B[i+1] = result
    
    # C 구하기
    print("=============== ci 구하기 ==============")
    c = getC(A,B)
    print(c)

    print("=============== di 구하기 ==============")
    # d 구하기
    d = []
    # di = ( ci(i+1) - ci(i) ) / 24
    # d1~5를 d 리스트에 삽입.
    
    for i in range(0,5):
        d.append( ( ci(i+1) - ci(i) ) / 24 )
    print(d)

    print("=============== bi 구하기 ==============")
    # b 구하기
    b = []
    # bi = ( 1/8 * (ai+1 - ai) - 8/3(ci+1 + 2*ci))
    for i in range(0,5):
        b.append( bi(ai(i),ai(i+1),ci(i),ci(i+1)) )
    print(b)

    print("=============== ai 구하기 ==============")
    a = []
    for i in range(0,5):
        a.append(ai(i))
    print(a)

    print("=============== 72~80 에서의 3차 스플라인을 통한 x = 75 예측 ==============")
    print(s5(75))
    

    


    

    
    
    