# 1987
# PyPy3로 채점함.

'''
내 예상 풀이
1. R,C를 입력받고, 2차원배열 board를 세팅한다.
2. x축 이동, y축 이동을 정의하는 dx, dy 배열을 선언한다.
3. board를 탐색하며 어떤 알파벳들을 마주쳤는지 정보를 담아둘 visited 리스트 선언. 길이는 알파벳 개수인 26만큼
    3-1. 알파벳들은 대문자 알파벳으로 주어진다. 만약 A라는 알파벳을 마주친 적이 있는지 확인하고 싶다면, visited(ord("A") - 65)로 접근하면 될 것이다.
4. dfs를 이용해 '얼마나 멀리 뻗어나갈 수 있는지'를 탐색한다.
    4.1 중복된 알파벳을 만나면 백트래킹
'''

import sys
input = sys.stdin.readline

def dfs(x,y,cnt):
    global max_cnt
    
    # 지금까지 탐색한 최대 길이가 현재 탐색한 위치까지의 길이보다 작다면, max_cnt를 갱신시켜준다.
    if max_cnt < cnt:
        max_cnt = cnt
    
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        # nx,ny가 바운더리를 벗어나지 않는 허용범위 내이고, 지금까지 마주친 적 없는 문자라면 수행한다.
        # 조건에 부합하지 않는다면 탈출 후 백트래킹
        if 0 <= nx < R and 0 <= ny < C and visited[ord(board[nx][ny]) - 65] == False:
            visited[ord(board[nx][ny]) - 65] = True
            dfs(nx,ny,cnt + 1)
            visited[ord(board[nx][ny]) - 65] = False

if __name__ == "__main__":
    # 1. R,C를 입력받고, 2차원배열 board를 세팅한다.
    R,C = map(int,input().split())
    board = []
    for i in range(R):
        board.append(list(map(str,input())))  
        del board[i][-1] 
    # 2. x축 이동, y축 이동을 정의하는 dx, dy 배열을 선언한다.
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 3. board를 탐색하며 어떤 알파벳들을 마주쳤는지 정보를 담아둘 visited 리스트 선언. 길이는 알파벳 개수인 26만큼
    visited = [False] * 26
    
    # 누적 개수(뻗어나간 길이)의 최대값을 담을 max_cnt. 1행 1열에서 시작하기에 초기값은 1
    # board의 1행 1열 알파벳 또한 방문여부 True로 변환
    max_cnt = 1
    visited[ord(board[0][0]) - 65] = True
    
    # 깊이우선탐색 수행. 초기 x,y값은 0,0이며 해당 위치에서 시작하기에 초기값은 1
    dfs(0,0,1)

    # dfs를 통해 최종적으로 산출된 max_cnt 값을 출력한다.
    print(max_cnt)
    
