# 14502

'''
1. 연구소 현재 상태를 lab에 저장. 벽이 세워질 수 있는 0인 공간 좌표를 따로 저장해둠
2. 벽 3개를 세울 수 있는 모든 경우의 수를 계산해서 가장 안전영역 크기가 큰 경우를 출력
'''

from collections import deque
import copy

def solution():
    global safezon_size
    wall_len = len(wall)

    for i in range(0, wall_len):
        for j in range(i + 1, wall_len):
            for k in range(j + 1, wall_len):
                safezon_size = max(safezon_size, bfs(wall[i], wall[j], wall[k]))
    
    print(safezon_size)


def bfs(point_1, point_2, point_3):
    temp_lab = copy.deepcopy(lab)
    # 벽 3개 세우기
    temp_lab[point_1[0]][point_1[1]] = temp_lab[point_2[0]][point_2[1]] = temp_lab[point_3[0]][point_3[1]] = 1
    
    queue.clear()
    for start_point in start:
        queue.append(start_point)
    
    while queue:
        now_v = queue.popleft()
        for idx in range(4):
            if isValid(temp_lab, now_v, dx[idx], dy[idx]):
                next_v = [now_v[0] + dy[idx], now_v[1] + dx[idx]]
                queue.append(next_v)
                temp_lab[next_v[0]][next_v[1]] = 2
    
    count = 0
    for row in range(N):
        for col in range(M):
            if temp_lab[row][col] == 0:
                count += 1
    
    return count


def isValid(temp_lab, now_v, dx, dy):
    if 0 <= now_v[0] + dy < N and 0 <= now_v[1] + dx < M:
        if temp_lab[now_v[0] + dy][now_v[1] + dx] == 0:
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    N, M = map(int, input().split())
    lab = []
    wall = []
    start = []
    for row in range(N):
        temp = list(map(int, input().split()))
        lab.append(temp)
        for col in range(M):
            if temp[col] == 0:
                wall.append([row, col])
            elif temp[col] == 2:
                start.append([row, col])
    
    safezon_size = -1
    queue = deque([])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    solution()