# 2118
'''
1. 입력받기 > 각 노드 간 거리를 1차원 배열로 받음 , 0번째 인덱스는 '0' 대입하며 더미 값 입력함
2. a - b 사이의 거리를 모든 경우의수에 대한 계산을 진행함 (두 포인터, 브루트포스)
2-1 a -> b까지 거리 : min(arr[a] + arr[a+1] + ... + arr[b-1] + arr[b]   , Total(모든 거리 더한 값) - 이전에 구한 거리 값
2-2 a -> c [ c = b + 1 ]까지 거리는 min(arr[a] + arr[a+1] + ... + arr[b] + arr[c] =  이전에 구한   , Total(모든 거리 더한 값) - 이전에 구한 거리 값)
3. 각 거리 중 가장 먼 max거리를 print
'''
# 위 방법은 시간초과

'''
a,b 두 지점을 적절하게 이동시켜 빠른 시간 내에 찾을 수 있지 않을까?

a,b 두 지점이 있을 때, 두 지점 사이 거리를 시계방향, 반시계방향 거리의 차가 0이거나 0에 가장 근접했을 때의 거리가 답임.
sumA : a,b 두 지점의 거리를 시계방향으로 거리를 구한 값, sumB : a,b 두 지점의 거리를 반시계방향으로 거리를 구한 값

1. sumA == sumB : 특정 두 지점 사이의 최댓값이므로 출력 및 종료
2. sumA < sumB : b를 시계방향으로 한 칸 이동하며, sumA의 값은 늘리고, sumB의 값을 줄임
3. sumA > sumB : a를 시계방향으로 한 칸 이동하며, sumA의 값을 줄이고, sumB의 값을 늘림
4. 2~3 과정을 반복하며 a가 다시 원점으로 돌아올 때까지 연산한다. sumA와 sumB의 값 차이가 최소일 때의 거리를 출력하면 된다.

a가 움직이는 최대 횟수 : N
b가 움직이는 최대 횟수 : 2N - 2
이론상 O(N) 복잡도를 지닌 풀이가 가능

'''
    
import sys

input = sys.stdin.readline

# 입력 받기 -> 각 노드 간 거리를 1차원 배열로 받음
N = int(input())

arr = [] # 각 지점간의 거리를 입력값으로 받을 배열 선언
total = 0 # 모든 거리의 합
for _ in range(N):
    temp = int(input())
    total += temp
    arr.append(temp)

a = 0 # 초기 a 위치
b = 1 # 초기 b 위치

sumA = arr[0] # sumA : a,b 두 지점의 거리를 시계방향으로 거리를 구한 값 
sumB = total - arr[0] # sumB : a,b 두 지점의 거리를 반시계방향으로 거리를 구한 값

dis_between = abs(sumA - sumB) # 두 지점 사이의 거리가 최소일 때의 두 점 사이의 최댓값
max_dis = min(sumA, sumB) # 최종적으로 구하고 싶은 최대거리값

while(a < N): # a가 움직일 때마다 cnt를 1씩 증가시킨다. cnt가 N 즉, a가 N번 움직이면 초기 위치로 돌아왔다는 것을 의미. 반복을 종료한다.

    # 1. sumA == sumB : 특정 두 지점 사이의 최댓값이므로 출력 및 종료
    if sumA == sumB:
        print(sumA)
        exit()
    # 2. sumA < sumB : b를 시계방향으로 한 칸 이동하며, sumA의 값은 늘리고, sumB의 값을 줄임
    if sumA < sumB: 
        sumA += arr[b]
        sumB -= arr[b]
        b += 1
        b %= N # b가 arr의 마지막 인덱스에 도달했을 때, 다시 0번째 인덱스로 돌아오게 하기 위한 mod 로직
    
    # 3. sumA > sumB : a를 시계방향으로 한 칸 이동하며, sumA의 값을 줄이고, sumB의 값을 늘림
    else:
        sumA -= arr[a]
        sumB += arr[a]
        a += 1
    if abs(sumA - sumB) < dis_between: # 시계/반시계 방향 거리의 차가 더 작으면
        dis_between = abs(sumA - sumB) # 거리 차 갱신
        max_dis = min(sumA,sumB) # 두 지점 사이의 거리 중 가장 짧은 거리를 최댓값으로 갱신

print(max_dis)

