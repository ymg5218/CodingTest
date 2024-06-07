# 프로그래머스 _ 평행

'''
1. 평행의 조건 : 두 선의 기울기가 같다.
1-1. 두 직선이 겹치는(일치하는) 경우에도 평행하다고 간주한다.
2. 점이 4개밖에 없으니 브루트포스 기법을 사용해도 무방하다.
2-1. 점 4개로 만들 수 있는 두 직선 : 3 가지
(dot1-dot2, dot3-dot4 || dot1-dot3, dot2-dot4 || dot1-dot4, dot2-dot3)

예상 풀이 방법
1. 모든 점 dot1, dot2, dot3, dot4를 입력받음
2. 두 점을 잇는 모든 경우의 수를 따져, 기울기가 같은 경우가 존재하는지 판단
3. 한 번이라도 평행인 경우가 존재하면 1, 없으면 0
'''
def solution(dots):
    if(inclination(dots[0],dots[1]) == inclination(dots[2],dots[3])):
        return 1
    if(inclination(dots[0],dots[2]) == inclination(dots[1],dots[3])):
        return 1
    if(inclination(dots[0],dots[3]) == inclination(dots[1],dots[2])):
        return 1
    return 0

def inclination(dot1,dot2):
    return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])

# dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
