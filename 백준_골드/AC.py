# 5430

'''
예상 풀이
1. 입력값 입력 받음.
1-1. 테스트 케이스 T
1-2. 수행할 함수 p
1-3. 배열에 들어있는 수의 개수 n
1-4. 배열에 들어있는 정수
2. 최초 삭제할 인덱스 : 0, R 메소드가 입력되어 뒤집을 때마다 뒤집힌 상태 변수(isReverse)를 True < - > False 로 바꾼다 : 매번 배열을 뒤집어, 수행시간 증가되는걸 막기 위함
3. D 메소드가 입력될 때마다 삭제할 인덱스 위치의 문자를 삭제.
3-1. D 메소드로 삭제할 때, 이미 빈 문자열이라면 error 출력
4. error 없이 연산을 모두 마쳤을 때, isReverse가 True라면 최종적으로 문자열을 뒤집어 출력.
4-1 isReverse가 False라면 문자열 그대로 출력
'''

import sys
from collections import deque
input = sys.stdin.readline

'''
 solution() : 입력받은 문자열 _arr을 _mthd 로직을 수행시킨 결과를 print 해주는 메소드
 매개변수
    - _mthd : 메소드들의 집합(로직)
    - _num_set : 입력받은 문자열. 로직에 의해 수행될 주체.
'''
def solution(_mthd, _num_set):
    cnt = 0 # R(뒤집기) 메소드의 호출 횟수. 최종적으로 홀수면 최종 큐를 뒤집어준다.
    d_point = 0 # 삭제할 인덱스. R이 호출될 때마다 isReverse를 True < - > False 로 바꾼다.
    isReverse = False # 현재 큐가 뒤집혔는지를 판단하는 bool 값
    
    for i in range(len(_mthd)):

        # D 메소드 호출 : d_point 인덱스 요소 삭제

        if _mthd[i] == 'D':
            try:
                # 뒤집힌 상태면 맨 마지막 문자를 없애야 함.
                if isReverse == True:
                    _num_set.pop()
                # 뒤집히지 않은 상태면 맨 첫번째 문자를 없애야 함.
                else:
                    _num_set.popleft()
            # 요소가 없는데 삭제를 시도하면 예외처리 : error 출력 후 함수 종료(return)
            except:
                print("error")
                return
            
        # R 메소드 호출 : 호출 될 때마다 isReverse를 True < - > False 로 바꾼다.
        elif _mthd[i] == "R":
            if isReverse == True:
                isReverse = False
            else:
                isReverse = True
    
    # isReverse == True 라면 최종 큐를 뒤집어준다.
    if isReverse == True:
        _num_set = list(_num_set)[::-1]
    print('[' + ','.join(_num_set) + ']')

if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        mthd = input() # 함수 입력받음
        length = int(input()) # 배열에 들어있는 수의 개수
        
        # [1,2,3,4] 자체를 문자열로 받기에 '[' 와 ']'를 제외한 상태로 ','를 기준으로 수를 큐 형태로 입력받는다.
        num_set = deque(input()[1:-2].split(','))

        # 빈 배열 [] 이 입력되었을 경우는 특이케이스로 []로 초기화시켰음
        if length == 0:
            num_set = ""
            
        solution(mthd,num_set)
        