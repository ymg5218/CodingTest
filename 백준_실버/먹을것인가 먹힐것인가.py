# 7795
'''
PyPy3로 채점함
1. 입력받음
2. A,B 리스트 입력받고 A는 오름차순, B는 내림차순
3. while문을 통해, A와 B 리스트 모두 앞에서부터 탐색
    3-1. 현재 탐색중인 A 요소와 B 요소를 비교했을 때, A 요소가 더 크면, B의 나머지 요소는 모두 A에게 잡아먹힘
    3-2. 아니라면 탐색중인 B 인덱스 + 1
    3-3 끝까지 탐색했다면 B 인덱스 0으로 초기화, A 인덱스 + 1
    3-4 A,B 모두 끝까지 탐색했다면 종료
4. 잡아먹힌 개수 프린트
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())

    A = list(map(int,input().split()))
    A.sort()

    B = list(map(int,input().split()))
    B.sort(reverse=True)

    cnt = 0
    a_idx = 0
    b_idx = 0
    while(a_idx < N and b_idx < M):
        if A[a_idx] > B[b_idx]:
            cnt += (M - b_idx)
            a_idx += 1
            b_idx = 0
            
        else:
            b_idx += 1

        if b_idx == M:
                a_idx += 1
                b_idx = 0


    print(cnt)