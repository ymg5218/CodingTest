# 수치해석 과제02 - 7번 문제 풀이용 코드
'''
코드 작성 일지 : 2023/05/07

코드 작성자 : 소프트웨어공학과 2017156019 염민규

코드 목적 : Newton의 2차 보간다항식을 활용하여 구간 내 특정 값을 근사한다.

구간 내 예측 값 P(x) = b1 + b2(x - x1) + b3(x - x1)(x - x2)

x0,x1,x2 세 점을 지나는 구간이라 가정

1. b1 = f(x0)
2. b2 = f[x1, x0] = (f(x1) - f(x0)) / (x1 - x0)
3. b3 = f[x2, x1, x0] = (f[x2, x1] - f[x1, x0]) / (x2 - x0)
      = 1 / (x2 - x0) * (((f(x2) - f(x1)) / (x2 - x1)) - ((f(x1) - f(x0)) / (x1 - x0)))
'''

# Newton의 2차 보간다항식을 활용하여 구간 내 특정 값을 근사
# 매개변수 : x0,x1,x2 각각의 f_x0, f_x1, f_x2 값
def newtondiff(f_x0, f_x1, f_x2):
    global x,x0,x1,x2
    
    b1 = f_x0
    b2 = (f_x1 - f_x0) / (x1 - x0)
    b3 = ( 1 / (x2 - x0) ) * (( ( f_x2 - f_x1 ) / ( x2 - x1 ) ) - ( ( f_x1 - f_x0 ) / ( x1 - x0 ) ))

    return b1 + b2 * (x - x0) + b3 * (x - x0) * (x - x1)



if __name__ == "__main__":
    
    # x0, x1, x2 정의, x = 1000이므로, x를 포함하는 세 점을 지나는 구간으로 선정
    x0 = 600
    x1 = 900
    x2 = 1200
    x = 1000 # 구하고자 하는 위치의 x 값

    # high_f_x : 높이에 대한 f(x)
    high_f_x0 = 112
    high_f_x1 = 130
    high_f_x2 = 150

    # resultHigh_by_newtonDiff : Newton의 2차 보간 다항식을 이용하여 구한 x = 1000 에서의 추정 높이 값
    resultHigh_by_newtonDiff = newtondiff(high_f_x0, high_f_x1, high_f_x2)
    print("x = 1000 에서의 추정 높이 : %.5f " %resultHigh_by_newtonDiff)

    # angle_f_x : 각도에 대한 f(x)
    angle_f_x0 = 41
    angle_f_x1 = 65
    angle_f_x2 = 78

    # resultAngle_by_newtonDiff : Newton의 2차 보간 다항식을 이용하여 구한 x = 1000 에서의 추정 각도 값
    resultAngle_by_newtonDiff = newtondiff(angle_f_x0, angle_f_x1, angle_f_x2)
    print("x = 1000 에서의 추정 각도 : %.5f " %resultAngle_by_newtonDiff)

    print("결과적으로, 1000초일 때 위성의 추정 위치는 높이 :  %.5f(m) , 각도 : %.5f(˚ ) 이다." %(resultHigh_by_newtonDiff, resultAngle_by_newtonDiff))
