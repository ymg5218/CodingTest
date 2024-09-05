# 15558
from collections import deque

def bfs():
    queue = deque()
    queue.append([0, 0])

    time = 0
    next_v = []
    while queue:
        while queue:
            now_line, now_idx = queue.popleft()
            # 현재 라인의 인덱스 번호에서 반대편 라인으로 k 만큼 점프해서 보드 바깥으로 나갈 수 있으면 클리어 가능.
            # 이는 한 칸 전진해서 보드 바깥으로 나가는 클리어 조건을 넓게 포괄하기에 이 조건만으로 충분하다고 판단.
            if now_idx + k >= N:
                return 1
            # 뒤로 한 칸 갈 수 있는지
            if now_idx > 0 and board[now_line][now_idx - 1] == "1" and now_idx - 1 > time:
                next_v.append([now_line, now_idx - 1])
                board[now_line][now_idx - 1] = "0"
            # 앞으로 한 칸 갈 수 있는지
            if board[now_line][now_idx + 1] == "1":
                next_v.append([now_line, now_idx + 1])
                board[now_line][now_idx + 1] = "0"
            # 반대편 라인으로 k 만큼 점프할 수 있는지
            if board[(now_line + 1) % 2][now_idx + k] == "1":
                next_v.append([(now_line + 1) % 2, now_idx + k])
                board[(now_line + 1) % 2][now_idx + k] = "0"

        while next_v:
            queue.append(next_v.pop())

        # 보드의 시작점 부분을 위험한 땅으로 분류
        board[0][time], board[1][time] = "0", "0"
        time += 1

    # 끝까지 클리어하지 못하면 0 return
    return 0

if __name__ == "__main__":
    N, k = map(int, input().split())
    board = []
    board.append(list(input()))
    board.append(list(input()))

    print(bfs())