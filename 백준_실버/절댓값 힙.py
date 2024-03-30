# 11286
'''
N회 연산을 진행.

1. 0이 아닌 값이 주어지면, 배열에 x라는 값을 추가
2. 0이 주어지면, 배열에서 절댓값이 가장 작은 값을 출력하고 배열에서 제거
'''

import sys, heapq
# 우선순위 큐 : 삽입 삭제 모두 O(lg(n))

input = sys.stdin.readline

def solution():
    # 큐
    queue = []

    for _ in range(N):
        x = int(input())
        if x != 0:
            heapq.heappush(queue, (abs(x), x))
        else:
            if not queue:
                print(0)
            else:
                print(heapq.heappop(queue)[1])

if __name__== "__main__":
    N = int(input())

    solution()