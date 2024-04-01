# 2531

import sys

input = sys.stdin.readline


'''
시간복잡도 : N * K -> 최악의 경우 90,000,000 ~= 10**8
'''
def solution():
    start_point = 0
    max_num = 0

    while True:
        if start_point == N:
            break
        
        # 먹는 경우의 수
        eat_case = []

        for i in range(k):
            # 탐색 좌표
            now_point = (start_point + i) % N
            eat_case.append(belt[now_point])

        # 쿠폰 초밥 먹기
        eat_case.append(c)

        # 중복 가짓수 제거 후, 기존 경우의 수보다 크면 갱신
        max_num = max(max_num, len(set(eat_case)))

        start_point += 1
    
    return max_num
            


if __name__ == "__main__":
    '''
    N : 벨트에 놓은 초밥 접시 수
    d : 초밥 가지 수
    k : 연속해서 먹는 접시의 수
    c : 쿠폰 번호
    '''
    N, d, k, c = map(int, input().split())

    belt = []

    for _ in range(N):
        belt.append(int(input()))
    
    print(solution())