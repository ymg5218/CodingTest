# 20208

# 10 2 3

# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 2 0 0 0 0 0 0
# 0 2 0 0 0 0 2 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 2 0 0 2 0 0 0 0 0
# 0 0 0 0 0 0 0 0 2 0
# 0 0 0 1 0 0 2 0 0 0
# 0 0 0 0 2 0 0 0 0 0
# 0 2 0 0 0 0 0 0 0 0
# 0 0 0 0 0 2 0 0 0 0

# 집 : (6,3)
# x나 y 값이 각기 1씩 변동될 때마다 체력 1 감소
# 민초우유 있는 각 x,y 값 - 진우 현재 위치 x,y값
# 각 x,y값의 절댓값의 합이 진우의 현재 체력을 넘어가면 안됨.

# 0. 민트초코를 먹을 수 있는 모든 경우의 수를 순열로 표현
# 참고 : https://velog.io/@beomsun/%EB%B0%B1%EC%A4%80-20208-%EC%A7%84%EC%9A%B0%EC%9D%98-%EB%AF%BC%ED%8A%B8%EC%B4%88%EC%BD%94
# 1. 현재 진우의 위치에서 첫 민초우유 위치로 가는 거리를 따져봄
# 2-1. 현재 체력으로 가장 가까운 민초우유 먹을 수 있는지 확인
# 2-2. 만약 그 민초우유를 먹었을 때 집으로 돌아올 수 있는지 확인
# 3. 돌아올 수 있으면 그 민초우유 먹고, 1~2-2 단계 반복
# 4. 만약 돌아올 수 없으면 마지막으로 먹은 민초우유의 위치로 backtracking
# 5. 1~4 단계를 계속 반복해 모든 민초우유 위치 탐색 후 결과 출력

def dfs(start):
    if start == len(fuck): # 모든 초코우유를 탐색했으면
        count(fuck_seq) # 해당 순열 갖고 count 시작
        return # count() 동작 끝냈으면 재귀호출된 해당 dfs()는 종료
    for i in range(0,len(fuck)):
        if not visited[i]: # 방문 안했으면
            visited[i] = True # 방문 했다고 표시
            fuck_seq.append(i)
            dfs(start + 1) # 다음 방문
            # 4. 만약 돌아올 수 없으면 마지막으로 먹은 민초우유의 위치로 backtracking
            visited[i] = False # 가봤는데 에바면 도르마무
            fuck_seq.pop() # 기록도 도르마무          
            

def count(fuck_seq): # 민초우유 몇개 먹을 수 있나 세보자
    global real_count
    now_m = M # 현재체력 저장

    # 현재 진우의 위치 : 초기값은 집 위치
    now_r = house[0][0] # 현재 진우의 행 위치
    now_c = house[0][1] # 현재 진우의 열 위치

    count = 0 # 현재 케이스에서 민초우유 먹개 먹었나 체크
    
    for fuck_loc in fuck_seq: # 각 경우의 수를 모두 따져봄

        fuck_r = fuck[fuck_loc][0] # 민초우유 행 위치
        fuck_c = fuck[fuck_loc][1] # 민초우유 열 위치

        # 1. 현재 진우의 위치에서 첫 민초우유 위치로 가는 거리를 따져본다
        dis = abs(fuck_r - now_r) + abs(fuck_c - now_c)

        # 2-1. 현재 체력으로 가장 가까운 민초우유 먹을 수 있는지 확인
        if dis > now_m: # 현재 체력으로 못 가는 거리면
            return # 과정을 끝낸다.
        
        now_m -= dis # 갈수 있다면 거리만큼 체력에서 빼고
        now_m += H # 민초우유 먹었으니 체력 증가
        count += 1 # 먹은 민초우유 개수도 증가

        # 2-2. 만약 그 민초우유를 먹었을 때 집으로 돌아올 수 있는지 확인
        callback = abs(fuck_r - house[0][0]) + abs(fuck_c - house[0][1])
        # 3. 돌아올 수 있으면 그 민초우유 먹고, 1~2-2 단계 반복
        if callback <= now_m:
            # 지금까지 모든 경우의 수 중, 가장 많이 먹은 민초우유 개수와 현재 케이스에서 먹은 민초우유 개수 중 더 많은 값 추출
            real_count = max(real_count,count)
        # 아직 집까지 못간다면 다음 시작 위치는 방금 먹은 민초우유 위치로 지정
        now_r = fuck_r
        now_c = fuck_c
        
        

if __name__ == "__main__":
    N,M,H = map(int,input().split())
    # N : 마을의 크기 N*N
    # M : 진우의 초기 체력
    # H : 민초우유 마실때 마다 증가하는 체력의 양
    
    real_count = 0 # 최종적으로 최대로 먹을 수 있는 민초우유 개수
    # N*N 크기의 마을 구조 입력받기
    village = [list(map(int, input().split())) for _ in range(0,N)]
    
    # 진우 집 어드레스 부르소
    house = [] # 진우 집 위치

    # 민초우유 위치값 배열에 저장
    fuck = [] # ㅈ같은 민트초코우유 위치
    for i in range(0,N):
        for j in range(0,N):
            if village[i][j] == 1:
                house.append([i,j])
            elif village[i][j] == 2:
                fuck.append([i,j])

    
    # dfs를 통한 민초우유 모든 방문 경우의 수 체크를 위함
    visited = [False] * len(fuck)
    fuck_seq = [] # 민초우유 먹는 모든 경우의 수
    
    dfs(0) # 모든 민초우유 방문하는 경우의 수 체크 시작
    
    # 5. 1~4 단계를 계속 반복해 모든 민초우유 위치 탐색 후 결과 출력
    print(real_count)
    
