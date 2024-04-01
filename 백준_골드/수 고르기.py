# 2230

import sys
input = sys.stdin.readline

def solution():
    l_point = 0
    r_point = 1
    
    # 최대 차이 수 : 10**9 - ( - 10**9 )
    min_gap = 2* 10**9 + 1

    # r_point가 배열 끝까지 탐색하도록 로직 구성
    while r_point < N:
        # l_point와 r_point가 같아지면 r_point를 1칸 밀기
        if l_point == r_point:
            r_point += 1
        else:
            gap = arr[r_point] - arr[l_point]
            if gap >= M:
                # 차이가 M일 경우, 최소값이기에 로직 종료
                if gap == M:
                    return gap
                
                # 차이가 M을 넘기면 min_gap과 비교하여 충족 시 갱신
                min_gap = min(min_gap, gap)
                l_point += 1
            else:
                r_point += 1
    
    return min_gap

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    arr = []

    for _ in range(N):
        arr.append(int(input()))
    
    # 정렬
    arr.sort()

    print(solution())