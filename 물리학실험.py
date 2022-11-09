import math

g = 9.8
m_a = 0.1

# 두 각도와 질량을 받아 F_x, F_y 를 반환하는 메소드
# 소숫점 셋 째 자리 까지 표시


def calc_force(B: tuple, C: tuple):
    force_x = round((B[1] * g * math.cos(B[0]*math.pi/180)) +
                    (C[1] * g * math.cos(C[0]*math.pi/180)), 3)
    force_y = round((B[1] * g * math.sin(B[0]*math.pi/180)) +
                    (C[1] * g * math.sin(C[0]*math.pi/180)), 3)
    return (force_x, force_y)

# F_x, F_y를 받아 m_A를 반환하는 메소드
# 소숫점 셋 째 자리 까지 표시


def calc_mass(force_x, force_y):
    m_a = round(math.sqrt(force_x**2 + force_y**2)/g, 3)
    return m_a

# 두 각도와 질량을 받아 해석법을 통한 m_A를 계산하는 메소드
# 소숫점 셋 째 자리 까지 표시


def calc_mass2(B, C):
    m_a = round(abs(math.sqrt(B[1]**2 + C[1] ** 2 + 2*B[1]*C[1]
                              * math.cos((B[0]*math.pi/180) - (C[0]*math.pi/180)))), 3)
    return m_a


# [(B의 각도, B의 질량), (C의 각도, C의 질량)] 쌍으로 이루어진 리스트
test_list = [
    [(203, 0.05), (165.5, 0.05)],
    [(210, 0.05), (150, 0.06)],
    [(219.5, 0.07), (135.5, 0.06)],
    [(233, 0.07), (134, 0.08)],
    [(232, 0.08), (128.5, 0.08)]
]

# x,y 좌표를 거리(kg)을 계산하는 메소드


def calc_euclid(x, y):
    length = round(math.sqrt(x**2 + y**2) / 100, 3)
    return length


xy_list = [
    (-9.4432624691527, -0.7017556221742),
    (-9.5262794416288, 0.5),
    (-11.2583302491977, -0.5),
    (-10.958639047386, 1.33021708607649),
    (-9.954088957062, -0.0432207740345)
]


check_m_a_list = []
check_m_a_error_list = []
if __name__ == "__main__":
    print("="*40)
    for A_ in xy_list:

        print(f"A'의 좌표 : {A_}")

        check_m_a = calc_euclid(A_[0], A_[1])
        check_m_a_list.append(check_m_a)
        check_m_a_error_list.append(abs(m_a-check_m_a)/m_a)

        print(f"check_m_a : {check_m_a}")

        print("="*40)


    print("해석법의 5회 평균값", round(sum(check_m_a_list)/5, 3))
    print(f"해석법의 평균 오차 {round(round(sum(check_m_a_error_list)/5,3)*100,3)}%")

    # print("="*40)
    # for test in test_list:
    #     B = test[0]
    #     C = test[1]

    #     print(f"B의 각도 : {B[0]}\tB의 질량 : {B[1]}")
    #     print(f"C의 각도 : {C[0]}\tC의 질량 : {C[1]}")

    #     check_m_a = calc_mass2(B,C)
    #     check_m_a_list.append(check_m_a)
    #     check_m_a_error_list.append(abs(m_a-check_m_a)/m_a)

    #     print(f"check_m_a : {check_m_a}")

    #     print("="*40)

    # print("해석법의 5회 평균값",round(sum(check_m_a_list)/5,3))
    # print(f"해석법의 평균 오차 {round(sum(check_m_a_error_list)/5,3)*100}%")

    # print("="*40)
    # for test in test_list:
    #     B = test[0]
    #     C = test[1]

    #     print(f"B의 각도 : {B[0]}\tB의 질량 : {B[1]}")
    #     print(f"C의 각도 : {C[0]}\tC의 질량 : {C[1]}")

    #     force_tuple = calc_force(B,C)

    #     print(f"F_x : {force_tuple[0]}\tF_y : {force_tuple[1]}")

    #     check_m_a = calc_mass(force_tuple[0],force_tuple[1])
    #     check_m_a_list.append(check_m_a)
    #     check_m_a_error_list.append(abs(m_a-check_m_a)/m_a)

    #     print(f"check_m_a : {check_m_a}")

    #     print("="*40)

    # print("분해법의 5회 평균값",round(sum(check_m_a_list)/5,3))
    # print(f"분해법의 평균 오차 {round(sum(check_m_a_error_list)/5,3)*100}%")
