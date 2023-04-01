# pypy3로 채점함

# 16958

import sys
input = sys.stdin.readline


'''
내 예상 풀이
1. 입력값 입력 받음
2. 2차원 평면 공간 graph = N * N size로 선언, 모든 값 MAX_DIS로 초기화
3. graph에 각 도시까지 거리 1차 계산
4. 중간에 특별한 도시를 거쳐가는 방식 고려해서 2차 계산
5. 출력
'''

MAX_DIS = 2001 # 각 도시간의 거리를 최댓값으로 초기화해주기 위함
# 1. 입력값 입력 받음
N,T = map(int,input().split())
special = []
city = []
for idx in range(N):
    info = list(map(int,input().split()))
    if info[0] == 1:
        special.append(idx)
    city.append(info)


# 2. 도시간 거리를 담아낼 그래프 선언 (size : N * N)
graph = [[MAX_DIS for _ in range(N)] for _ in range(N)]

# 3. 그래프에 각 도시간의 거리를 계산

for row in range(N):
    for col in range(row + 1, N): # 어차피 대각선 대칭이기 때문에, 모든 값을 구할 필요는 없음
        dis = (abs(city[row][1] - city[col][1]) + abs(city[row][2] - city[col][2])) # 두 도시간의 거리
        if city[row][0] == 1 and city[col][0] == 1: # 둘다 특별한 도시면
            if T <= dis:
                graph[row][col] = T
                graph[col][row] = T
            else:
                graph[row][col] = dis
                graph[col][row] = dis
        else:
            graph[row][col] = dis
            graph[col][row] = dis

# 4. 중간에 특별한 도시를 거쳐 가는 방식 고려해서 그래프값 갱신

for row in range(N):
    for col in range(row + 1, N): # 어차피 대각선 대칭이기 때문에, 모든 값을 구할 필요는 없음
        if city[row][0] == 1 and city[col][0] == 1: # 둘다 특별한 도시면
            continue # 이미 최솟값이기에 연산 생략한다.
        elif city[row][0] == 1 and city[col][0] == 0: # A도시가 특별하고 B도시는 평범하면
            temp_special = special[:]
            temp_special.remove(row)
            near = 2001
            # B에서 가장 가까운 특별한 도시 찾기
            for i in range(len(temp_special)):
                near = min(near,graph[col][temp_special[i]])
            
            # A -> B에서 가장 가까운 특별한 도시 -> B 거리가 기존 A -> B 거리보다 가까운지 판단
            graph[row][col] = min(near + T, graph[row][col])
            graph[col][row] = min(near + T, graph[row][col])

        elif city[row][0] == 0 and city[col][0] == 1: # A도시가 평범하고 B도시는 특별하면
            temp_special = special[:]
            temp_special.remove(col)
            near = 2001
            # A에서 가장 가까운 특별한 도시 찾기
            for i in range(len(temp_special)):
                near = min(near,graph[row][temp_special[i]])
            
            # A -> B에서 가장 가까운 특별한 도시 -> B 거리가 기존 A -> B 거리보다 가까운지 판단
            graph[row][col] = min(near + T, graph[row][col])
            graph[col][row] = min(near + T, graph[row][col])

        else: # A,B 모두 특별한 도시가 아님
            temp_special = special[:]
            near_A = 2001
            near_B = 2001
            # A,B 각각에서 가장 가까운 특별한 도시 찾기
            for i in range(len(temp_special)):
                # A에서 가장 가까운 특별한 도시 찾기
                near_A = min(near_A,graph[row][temp_special[i]])

                # B에서 가장 가까운 특별한 도시 찾기
                near_B = min(near_B,graph[col][temp_special[i]])
                
            
            # A -> B에서 가장 가까운 특별한 도시 -> B 거리가 기존 A -> B 거리보다 가까운지 판단
            graph[row][col] = min(near_A + T + near_B, graph[row][col])
            graph[col][row] = min(near_A + T + near_B, graph[row][col])

# 5. 출력
M = int(input())

for _ in range(M):
    city_A, city_B = map(int,input().split())
    print(graph[city_A - 1][city_B - 1])
            
        
        
