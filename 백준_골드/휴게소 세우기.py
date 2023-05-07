# 1477

'''
내 예상 풀이
1. 입력 값을 입력받음
2. 설치할 휴게소 간 거리를 구하기 위한 이분탐색을 위해 start = 1, end = L로 선언. mid = (start + end) // 2 로 선언하며, mid는 설치할 휴게소 간 거리 추정 값이다.
3. 각 구간의 거리에 mid 간격으로 휴게소를 설치할 때 몇 개를 설치할 수 있는지를 합산한다.
    3-1. 합산 값이 M보다 크면 너무 많이 설치할 수 있으므로 이보다 더 적게 설치하기 위해 mid를 키워야 함 : start = mid + 1 으로 재선언
    3-2. 합산 값이 M보다 작으면 더 설치할 수 있으므로 이보다 더 많이 설치하기 위해 mid를 줄여야 함 : end = mid - 1으로 재선언
    3-3. 합산 값이 M과 같으면 간격의 길이를 더 최소화 할 수 있는지 검사하기 위해 mid를 줄여본다 : end = mid - 1
4. start가 end보다 커지는 순간, 이분탐색을 멈추며, 마무리는 항상 3-3 과정을 통해 거리를 조금씩 줄이다 끝나기 때문에, 탐색 종료 시점 가장 최근의 mid값이 곧 원하는 출력 값이다.
'''

'''
함수 명 : solution
매개변수
    - start : 이분탐색을 위한 구간 중 최소점
    - end : 이분탐색을 위한 구간 중 최대점
역할 : 새로운 휴게소 M개를 지었을 때, 휴게소가 없는 구간의 최댓값의 최솟값을 출력해준다. 
'''
def solution(start,end):
    global M
    global locate

    if start > end: # 이분탐색 종료
        print(start) # 최종 start 값이 휴게소가 없는 구간의 최댓값의 최솟값
        return
    mid = (start + end) // 2 # mid : 새로지을 휴게소 간의 간격
    sum = 0 # sum : 휴게소 간의 간격을 mid로 책정했을 때, 세울 수 있는 총 휴게소의 개수

    # 각 지점 사이 휴게소를 설치할 때, mid 간격으로 휴게소를 설치하면 몇 개 설치할 수 있는지 검사
    for i in range(1,len(locate)): 
        sum += (locate[i] - locate[i-1] - 1) // mid # 이미 휴게소가 있는 지점은 설치할 수 없기에 각 지점 간 거리에서 1을 추가로 빼준다.

    # 합산 값이 M보다 크면 너무 많이 설치할 수 있으므로 mid를 줄여야 함 : end = mid - 1으로 재선언
    if sum > M:
        start = mid + 1
        solution(start, end)

    # 합산 값이 M보다 작으면 더 설치할 수 있으므로 이보다 더 많이 설치하기 위해 mid를 줄여야 함 : end = mid - 1으로 재선언
    # 합산 값이 M과 같으면 간격의 길이를 더 최소화 할 수 있는지 검사하기 위해 mid를 줄여본다 : end = mid - 1
    else:
        end = mid - 1
        if start > end: # 이분 탐색 종료
            print(mid)
            exit()
        solution(start, end)
        

if __name__ == "__main__":
    N,M,L = map(int,input().split())
    
    locate = list(map(int,input().split())) 
    locate.append(0), locate.append(L) # 고속도로의 시작점과 끝점 또한 휴게소를 설치할 수 없기에 휴게소와 같은 '특정 지점'으로 인식
    locate.sort() # 위치 순으로 오름차순 정렬

    # start = 1, end = L 로 초기값 세팅
    # start를  0이 아닌 1로 두는 이유
    # start가 0일 경우, ZeroDivisionError 유발 가능성을 가진 예외가 생김
    solution(0,locate[-1])
     

    