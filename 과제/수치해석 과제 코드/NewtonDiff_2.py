# 수치해석 과제02 - 9번 문제 풀이용 코드
'''
코드 작성 일지 : 2023/05/08

코드 작성자 : 소프트웨어공학과 2017156019 염민규

코드 목적 : Newton의 5차 보간다항식을 활용하여 구간 내 특정 값을 근사한다.

구간 내 예측 값 P(x) = b1 + b2(x - x1) + b3(x - x1)(x - x2) + b4(x - x1)(x - x2)(x - x3) 
                                + b5(x - x1)(x - x2)(x - x3)(x - x4) + b6(x - x1)(x - x2)(x - x3)(x - x4)(x - x5)

x0,x1,x2,x3,x4,x5 여섯 개의 점을 지나는 구간

1. b1 = f(x0)
2. b2 = f[x1, x0] = (f(x1) - f(x0)) / (x1 - x0)
3. b3 = f[x2, x1, x0] = (f[x2, x1] - f[x1, x0]) / (x2 - x0)
4. b4 = f[x3, x2, x1, x0] = (f[x3, x2, x1] - f[x2, x1, x0]) / (x3 - x0)
5. b5 = f[x4, x3, x2, x1, x0] = (f[x4, x3, x2, x1] - f[x3, x2, x1, x0]) / (x4 - x0)
6. b6 = f[x5, x4, x3, x2, x1, x0] = (f[x5, x4, x3, x2, x1] - f[x4, x3, x2, x1, x0]) / (x5 - x0)
'''

'''
b1 = f(x0)
'''
def get_b1(i1):
    global Y
    return Y[i1]

'''
b2 = f[x1, x0] = (f(x1) - f(x0)) / (x1 - x0)
'''
def get_b2(i1,i2):
    global X,Y
    global b1
    return (get_b1(i2) - get_b1(i1)) / (X[i2] - X[i1])

'''
b3 = f[x2, x1, x0] = (f[x2, x1] - f[x1, x0]) / (x2 - x0)
'''
def get_b3(i1,i2,i3):
    global X,Y
    global b2
    return (get_b2(i2,i3) - get_b2(i1,i2)) / (X[i3] - X[i1])

'''
b4 = f[x3, x2, x1, x0] = (f[x3, x2, x1] - f[x2, x1, x0]) / (x3 - x0)
'''

def get_b4(i1,i2,i3,i4):
    global X,Y
    return (get_b3(i2,i3,i4) - get_b3(i1,i2,i3)) / (X[i4] - X[i1])

'''
b5 = f[x4, x3, x2, x1, x0] = (f[x4, x3, x2, x1] - f[x3, x2, x1, x0]) / (x4 - x0)
'''
def get_b5(i1,i2,i3,i4,i5):
    global X,Y
    return (get_b4(i2,i3,i4,i5) - get_b4(i1,i2,i3,i4)) / (X[i5] - X[i1])

'''
b6 = f[x5, x4, x3, x2, x1, x0] = (f[x5, x4, x3, x2, x1] - f[x4, x3, x2, x1, x0]) / (x5 - x0)
'''
def get_b6(i1,i2,i3,i4,i5,i6):
    global X,Y
    global b5
    return (get_b5(i2,i3,i4,i5,i6) - get_b5(i1,i2,i3,i4,i5)) / (X[i6] - X[i1])

'''
P(x) = b1 + b2(x - x1) + b3(x - x1)(x - x2) + b4(x - x1)(x - x2)(x - x3) 
       + b5(x - x1)(x - x2)(x - x3)(x - x4) + b6(x - x1)(x - x2)(x - x3)(x - x4)(x - x5)
'''
def p(x):
    global b1,b2,b3,b4,b5,b6
    global X
    
    # return 형식이 너무 길어, 자르기 위해 임의로 _a, _b로 나눔
    _a = b1 + b2*(x - X[0]) + b3*(x - X[0])*(x - X[1]) + b4*(x - X[0])*(x - X[1])*(x - X[2])
    _b = b5*(x - X[0])*(x - X[1])*(x - X[2])*(x - X[3]) + b6*(x - X[0])*(x - X[1])*(x - X[2])*(x - X[3])*(x - X[4])
    return _a + _b

if __name__ == "__main__":
    
    # 여섯개의 (X,Y)쌍을 받음
    X = [-0.5, -0.25, 0 , 0.25, 0.5, 1]
    Y = [-41, -13.5625, -193, 13.5625, 41, 193]
    # x = 0.1 에서의 전압 V를 알고 싶음
    x = 0.1

    b1 = get_b1(0)
    b2 = get_b2(0,1)
    b3 = get_b3(0,1,2)
    b4 = get_b4(0,1,2,3)
    b5 = get_b5(0,1,2,3,4)
    b6 = get_b6(0,1,2,3,4,5)

    result_V = p(x)
    print("i = %.1f 에 대한 전압 V는 약 %.5f 이다. "%(x, result_V))

    