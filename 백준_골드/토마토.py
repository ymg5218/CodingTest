# 7576

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    global no_tomato
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    queue = deque()

    # day : 경과 시간(단위 : 1일)
    day = 0

    # 토마토가 최초로 익은 지점을 큐에 저장
    for idx in range(len(tomato)):
        queue.append(tomato[idx])
    
    # 다음으로 토마토가 익을 예정인 토마토 좌표들을 담을 next_v 리스트
    next_v = []

    # 최종적으로 큐가 빌 때까지( 더 이상 탐색이 불가능 할 때까지 ) 반복
    while queue:
        # 다음 토마토가 익을 위치는 매 반복문 시작할 때마다 초기화
        next_v.clear()
        # 익을 예정인 토마토들은 익도록 하고, 다음 익을 예정인 토마토들을 next_v에 담는 과정
        # 익을 예정인 토마토들이 모두 익을 때까지 반복
        while queue:
            # now_v : 현재 막 익은 토마토의 좌표 정보
            now_v = queue.popleft()
            # 상하좌우에 아직 안 익은 토마토가 있는지 확인. 있다면 next_v에 append
            for i in range(4):
                if isValid(now_v, dx[i], dy[i]):
                    next_v.append([now_v[0] + dy[i], now_v[1] + dx[i]])
                    table[now_v[0] + dy[i]][now_v[1] + dx[i]] = 1
        
        # 다음에 익을 후보 토마토들을 queue에 저장
        for v in next_v:
            queue.append(v)
            # 익을 후보 토마토들 개수만큼 no_tomato 1씩 차감
            no_tomato -= 1

        # 하루 경과
        day += 1
     
    if no_tomato > 0 :
        print(-1)
    else:
        # 위의 로직대로면 더 익을 토마토가 없는 마지막 날에 하루를 또 더해버리기에 day에서 1을 차감해 출력
        print(day - 1)
        

# 상하좌우로 한 칸씩 움직일 수 있는지, 움직일 수 있다면 아직 익지 않은 토마토가 있는지 확인하는 메소드
def isValid(now_v, dx, dy):
    if 0 <= now_v[0] + dy < N and 0 <= now_v[1] + dx < M:
        if table[now_v[0] + dy][now_v[1] + dx] == 0:
            return True
        else: return False
    else:
        return False
 

if __name__ == "__main__":
    M, N = map(int, input().split())

    # 토마토 창고를 표현할 2차원 테이블 선언
    table = []

    # 익은 토마토의 위치를 담을 리스트 선언
    tomato = []
    
    # 익지 않은 토마토의 개수를 담을 no_tomato
    # 탐색이 끝나도 no_tomato가 1개 이상 남아있다면, -1을 출력하기 위함
    no_tomato = 0
    # 테이블 세팅 및 익은 토마토 위치 저장
    for row in range(N):
        _row = list(map(int, input().split()))
        table.append(_row)
        for col in range(M):
            if _row[col] == 1:
                tomato.append([row, col])
            elif _row[col] == 0:
                no_tomato += 1
    
    # 너비우선탐색 시작
    bfs()
    
    