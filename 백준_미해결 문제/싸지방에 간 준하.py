# 12764

# 시작 시간과 종료 시간은 겹치지 않음
# 시작 시간 순서대로 빈자리 중, 앞에서부터 자리를 채움

# 파이썬 - 우선순위 큐 내장 함수 사용 : https://dev-ku.tistory.com/250

import sys
from queue import PriorityQueue # 우선순위 큐 내장모듈 임포트

input = sys.stdin.readline # 편법 on

def solution():
    global real_cnt

    while use_arr:
        # 큐 비어있으면 종료
        if use_arr.empty():
            break
        
        temp = use_arr.get() # 우선순위 높은 요소 (= 사용 시작 시간이 가장 빠른 사람)를 get()
        for i in range(len(computer)): # 사용중인 컴퓨터 탐색
            if computer[i] <= temp[0]: 
                if computer[i] == -1: # 한 번도 사용 안했던 컴퓨터를 사용하는 거라면?
                    real_cnt += 1 # 사용감 있는 컴퓨터 개수 증가
                computer[i] = temp[1] # 좌석
                count[i] += 1
                break
        


X = int(input()) # 사람의 수 입력

use_arr = PriorityQueue(maxsize = X) # 우선순위 큐의 최대사이즈 지정

computer = [-1] * X # 컴퓨터 사용중 여부 
count = [0] * X # 컴퓨터 사용 횟수 -> 출력에 이용될 배열
real_cnt = 0 # 사용감 있는 컴퓨터 개수

for i in range(X): # 사용 시작 시간과 종료 시간 입력받기
    start, end = map(int,input().split())
    use_arr.put((start,end))


# 솔루션 함수 실행
solution()

print(real_cnt) # 첫째줄에 사용감 있는 컴퓨터 개수 출력

for i in count: # 둘째줄에 사용한 컴퓨터들의 각자 횟수 출력
    if i == 0:
        break
    print(i, end=" ")
