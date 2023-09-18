# 3190

'''
https://www.acmicpc.net/board/view/109911

1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다. 그 후에 꼬리 길이를 줄이는 것이다. 따라서 꼬리를 줄이기 이전에 뱀이 부딪힐 수 있다. 
2. 사과는 먹으면 없어진다.
3. 8 D 라는 뜻은 8초가 지난 후(9초가 시작함과 동시)에 오른쪽으로 방향을 튼다는 뜻이다.
4. 1행 1열부터 시작이다.
'''

'''
흐름도
1. 입력값 입력받고, 2차원배열 세팅

2. dx, dy 선언한다 [오른쪽, 아래, 왼쪽, 위] 순서로 세팅
    -> dx = [1, 0, -1 , 0]
    -> dy = [0, -1, 0, 1]
    dx,dy의 인덱스를 가리키는 forward라는 변수를 선언, 초기값 0. dx = 1, dy = 0을 가리켜 오른쪽을 향하게 함
    만약 처음으로 D가 등장하면 forward를 1 증가시켜, dx = 0, dy = -1을 가리키게 함

3. 뱀의 몸이 차지하는 좌표 정보를 담기 위해 큐로 선언한다.

4. time을 1씩 증가시켜, dx와 dy쌍이 가리키는 방향으로 계속 움직인다. 대신, 다음과 같은 플로우를 지키도록 한다.
    4-1. 머리쪽 길이를 1 증가시킨다
    4-2. 꼬리쪽 길이를 1 감소시킨다.

    만약 [[1,1], [1,2], [1,3]]을 차지하는 길이 3의 뱀이 오른쪽으로 한 칸 움직인다면 다음과 같이 진행될 것이다.
    -1. 큐의 마지막 인덱스 위치에 [1,4]를 append
    -2. 큐의 0번째 인덱스 위치의 [1,1]를 popleft
    -3. 만약 append한 좌표가 이미 뱀이 차지하는 좌표와 같다 or 2차원 배열 범위를 벗어났다 => 게임 종료

5. 해당 위치에 사과가 있으면 머리쪽 길이를 1 증가시킨다. = 사과 위치의 인덱스를 append한다.
    만약 머리쪽 길이가 1 증가됐을 때 추가로 차지하는 위치가 이미 뱀이 차지하는 좌표와 같다 or 2차원 배열 범위를 벗어났다 => 게임 종료

'''

from collections import deque
import sys

input = sys.stdin.readline

def solution():
    # 2. dx, dy 선언
    # 오른쪽, 아래쪽, 왼쪽, 위쪽
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 현재 움직이는 위치를 가리킬 forward 선언.
    # dx, dy 인덱스 쌍을 가리켜, 현재 이동방향의 기준이 될 것
    forward = 0 

    # 3. 뱀이 현재 차지하고 있는 좌표정보를 담을 큐 형태의 자료구조 선언
    # 뱀의 첫 시작위치는 [0,0]이니 미리 추가해줌.
    snake = deque([[0, 0]])

    L = int(input())
    # 뱀의 방향정보를 담을 큐 선언
    goto_info = deque([])
    for _ in range(L):
        goto_time, goto_forward = map(str,input().split())
        goto_info.append([int(goto_time),goto_forward])
    
    # 게임 경과 시간. 만약 게임오버 된다면, time을 출력해야 한다.
    time = 0

    # 4. time을 1씩 증가시켜, dx와 dy쌍이 가리키는 방향으로 계속 움직인다.
    while(1):
        time += 1
        # 현재 진행방향으로 머리를 한 칸 늘린다.
        head = [snake[-1][0] + dy[forward], snake[-1][1] + dx[forward]]
        
        # 머리를 한 칸 늘렸을 때, 자신의 몸이나 벽에 부딪혔다면 게임종료
        if isGameOver(snake, head):
            return time
        # 아니라면 snake에 정상적으로 append하여 진행방향만큼 1 전진
        else:
            snake.append(head)

        # 만약 사과를 먹지 않았다면 꼬리를 1만큼 제거
        if board[head[0]][head[1]] == 0:
            snake.popleft()
        # 만약 사과를 먹었다면 사과 위치의 값을 1에서 0으로 변경
        # 꼬리는 제거하지 않음
        else:
            board[head[0]][head[1]] = 0

        # 진행방향을 바꿔야하는지 확인
        if goto_info and time == goto_info[0][0]:
            if goto_info[0][1] == "D":
                forward = (forward + 1) % 4
            else:
                if forward == 0:
                    forward = 3
                else:
                    forward -= 1
            goto_info.popleft()
            

# 게임종료 조건을 확인하는 메소드
def isGameOver(snack, head):
    if head in snack:
        return True
    elif head[0] >= N or head[0] < 0 or head[1] >= N or head[1] < 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    # 1. N, K, 사과위치 입력 받고 2차원 배열 세팅
    N = int(input())
    board = [ [0 for _ in range(N)] for _ in range(N)]
    
    # 사과 위치 세팅. 사과가 있는 곳은 1로 표시한다.
    K = int(input())
    for _ in range(K):
        apple_x, apple_y = map(int,input().split())
        board[apple_x - 1][apple_y - 1] = 1

    print(solution())