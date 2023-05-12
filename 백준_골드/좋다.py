# 1253

'''
내 예상 풀이
1. 입력받은 배열을 오름차순으로 정렬
2. 로직을 수행할 solution() 함수 수행. 매개변수 : "GOOD"인 수가 몇개인지 확인할 리스트
3. 0번째 인덱스 요소부터 '조건에 부합하는 수'인지 확인할 test라는 변수에 대입
4. 가장 첫 번째 인덱스 0을 left, 가장 마지막 인덱스 N-1을 right로 가정
    4-1 left < right 일 때 까지만 반복문 수행 (left = right까지 허용해버리면, 같은 수 + 같은 수 조합이 생기므로 예외경우 발생)
    4-2 left 혹은 right 둘 중 하나가 현재 검사중인 test의 인덱스 위치와 같을 수 있음
        4-2-1. left가 test의 인덱스와 같은 경우였다면, left + 1
        4-2-2. right가 test의 인덱스와 같은 경우였다면, right - 1
    4-3 arr[left] + arr[right] < test인 경우, 수가 left + 1
    4-4 arr[left] + arr[right] > test인 경우, right - 1
    4-5 arr[left] + arr[right] = test인 경우 "좋은 수" 개수 + 1, dp에 test 추가 후 break
        4-5-2. left가 test의 인덱스와 같은 경우였다면, left + 1
        4-5-3. right가 test의 인덱스와 같은 경우였다면, right - 1
5. test 위치를 한 칸씩 밀며 4의 과정을 반복 수행
6. 누적된 cnt 출력

'''

import sys
input = sys.stdin.readline


def solution(_arr):
    global cnt
    global dp
    for i in range(N):
        test = _arr[i]
        # 현재 test할 요소가 dp안에 이미 있는, "좋은 수"라면, 로직 수행하지 말고 cnt + 1, 다음 요소로 건너 뜀
        if test in dp:
            cnt += 1
            continue
        left = 0
        right = N-1
        while(left < right):
            # left나 right가 현재 검사중인 test의 인덱스와 같아질 경우, 적절한 조치 후 continue
            if left == i:
                left += 1
                continue
            elif right == i:
                right -= 1
                continue
            # left, right가 현재 검사중인 test의 인덱스와 같지 않음이 확인된 이후 로직 수행
            else:
                # [left] + [right]가 test보다 작다면, 합한 수를 키우기 위해 left + 1
                if _arr[left] + _arr[right] < test:
                    left += 1
                # [left] + [right]가 test보다 크다면, 합한 수를 줄이기 위해 right - 1
                elif arr[left] + arr[right] > test:
                    right -= 1
                # [left] + [right]가 test와 같다면, dp에 저장 및 cnt + 1
                else:
                    if left != i and right != i: # 자기 자신은 피연산자로 쓰이면 안됨
                        dp.append(test)
                        cnt += 1
                    break

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    dp = [] # 좋은 수를 담을 dp. test할 요소가 dp에 있으면 로직을 반복수행하지 않고 바로 수를 누적시키기 위함
    cnt = 0 # "좋은 수"가 몇 개인지 누적시킬 변수
    solution(arr)

    print(cnt)