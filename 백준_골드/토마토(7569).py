# 7569

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global early_tomato

    # 오른쪽, 아래, 왼쪽, 위
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]
    
    # 위 상자, 아래 상자
    d_box = [-1, 1]
    next_queue = deque([])
    # 경과 날짜
    day = 0
    # 토마토 익는 로직 시작
   

    while queue:
        while queue:
            now_tomato = queue.popleft()
            now_box = now_tomato[0]
            now_row = now_tomato[1]
            now_col = now_tomato[2]
            for i in range(4):
                if is_valid(now_box, now_row + d_row[i], now_col + d_col[i]):
                    next_queue.append([now_box, now_row + d_row[i], now_col + d_col[i]])
                    tomato[now_box][now_row + d_row[i]][now_col + d_col[i]] = 1
                    early_tomato -= 1
            
            for j in range(2):
                if is_valid2(now_box + d_box[j], now_row, now_col):
                    next_queue.append([now_box + d_box[j], now_row, now_col])
                    tomato[now_box + d_box[j]][now_row][now_col] = 1
                    early_tomato -= 1

        while next_queue:
            queue.append(next_queue.popleft())

        # 다음 날 익을 토마토 확인 : 하루가 지나있음을 의미
        day += 1


    if early_tomato != 0:
        print(-1)
    else:
        print(day - 1)
    


def is_valid(box, row, col):
    if 0 <= col < M and 0 <= row < N:
        if tomato[box][row][col] == 0:
            return True
        else:
            return False
    else:
        return False

def is_valid2(box, row, col):
    if 0 <= box < H and 0 <= col < M and 0 <= row < N:
        if tomato[box][row][col] == 0:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    M, N, H = map(int, input().split())

    queue = deque([])

    tomato = [[]for _ in range(H)]

    # 아직 익지 않은 토마토 개수
    early_tomato = 0
    # i : i번째 토마토 상자
    for i in range(H):
        # j : i 번째 토마토 판의 j행 토마토들
        for j in range(N):
            row = list(map(int, input().split()))
            tomato[i].append(row)
            # k : i번쨰 토마토 판의 j행의 k열 토마토
            for k in range(M):
                # 익은 토마토를 queue에 추가
                if row[k] == 1:
                    queue.append([i, j, k])
                # 익지 않은 토마토라면 개수 1 증가
                elif row[k] == 0:
                    early_tomato += 1

    bfs()