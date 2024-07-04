from collections import deque

def isValid(row, col):
    global visited
    global total_row
    global total_col

    if 0 <= row < total_row and 0 <= col < total_col:
        if not visited[row][col]:
            return True

    return False

def solution(maps):
    global total_row
    global total_col
    global visited

    total_row = len(maps)
    total_col = len(maps[0])

    # 북 동 남 서
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    queue = deque()
    # 다음 턴에 방문하게 될 노드들을 담을 배열
    next_v = []
    visited = [[False for _ in range(total_col)] for _ in range(total_row)]

    queue.append([0, 0])
    visited[0][0] = True

    distance = 1
    while queue:
        next_v.clear()
        while queue:
            now_row, now_col = queue.popleft()

            for i in range(4):
                next_row = now_row + d_row[i]
                next_col = now_col + d_col[i]
                if isValid(next_row, next_col):
                    if maps[next_row][next_col] == 1:
                        next_v.append([next_row, next_col])
                        visited[next_row][next_col] = True

        while next_v:
            v = next_v.pop();
            if v[0] == total_row - 1 and v[1] == total_col - 1:
                return distance + 1
            queue.append(v)
        distance += 1

    # while문 안에서 [n, m]까지 도달하지 못했다면 갈 수 없는 좌표임.
    return -1

if __name__ == "__main__":
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))