# 1074

# 2^15 * 2^15 가 최대 2차원 배열의 크기 => 벌써부터 배열로 선언하면 ㅈ될꺼 같음

'''
내 예상 풀이과정
1. 전체 2차원공간을 정확히 4등분(사분면)으로 나눈다.
2. 주어진 행과 열을 비교하여, 몇 사분면인지 판단한다.
3. 해당 사분면의 첫번째 인덱스는 몇 번째로 탐색되는지 알아낸다.
<반복>
4. 주어진 공간에서 또 4등분(사분면)으로 나눈다.
5. 주어진 행과 열을 비교하여, 몇 사분면인지 판단한다
6. 해당 사분면의 첫번째 인덱스는 몇 번째로 탐색되는지 알아낸다.
.
.
.
7. 더 나누어지지 않는 최소영역단위에서의 최종 값이 원하는 값
'''


N,r,c = map(int,input().split())

start = 0 # 전체 영역에서 가장 왼쪽 위(첫 번째) 위치 인덱스의 탐색 순서

# 행과 열을 2로 나눈 값을 기준 행/열로 선언
standard_r = 2**(N-1)
standard_c = 2**(N-1)

while(N > 0):
    N -= 1

    if r < standard_r and c >= standard_c: # 제 1사분면
        start += (2 ** N) * (2 ** N) * 1 # 제 1사분면 영역의 가장 첫번째 위치 탐색 순서
        # 해당 범위에서 4개의 영역으로 자르기 위함
        # 1사분면은 행은 기존과 같은 형식이나, 열이 그렇지 못함.
        standard_r -= (2**N//2)
        standard_c += (2**N//2)
        #print("제 1사분면",end=" ")
        #print(standard_r, standard_c)
    
    elif r < standard_r and c < standard_c: # 제 2사분면
        start += (2 ** N) * (2 ** N) * 0 # 제 2사분면 영역의 가장 첫번째 위치 탐색 순서
        # 해당 범위에서 4개의 영역으로 자르기 위함
        # 허나, 2사분면은 행과 열이 기존과 같은 형식이라 건들지 않음.
        # 다음 영역으로 자르기 위해, 기존 기준값들을 모두 줄여준다
        standard_r -= (2**N//2)
        standard_c -= (2**N//2)
        #print("제 2사분면",end=" ")
        #print(standard_r, standard_c)
    elif r >= standard_r and c < standard_c : # 제 3사분면
        start += (2 ** N) * (2 ** N) * 2 # 제 3사분면 영역의 가장 첫번째 위치 탐색 순서
        standard_r += (2**N//2)
        standard_c -=(2**N//2)
        #print("제 3사분면",end=" ")
        #print(standard_r, standard_c)
    else: # 제 4사분면
        start += (2 ** N) * (2 ** N) * 3 # 제 4사분면 영역의 가장 첫번째 위치 탐색 순서
        standard_r += (2**N//2)
        standard_c += (2**N//2)
        #print("제 4사분면",end=" ")
        #print(standard_r, standard_c)

print(start)