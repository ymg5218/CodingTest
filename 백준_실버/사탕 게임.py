# 3085
def findMaxCandy():
    global maxCnt

    # 행 탐색
    for row in range(N):
        nowCnt = 0
        nowColor = ""
        for col in range(N):
            if nowColor != board[row][col]:
                maxCnt = max(maxCnt, nowCnt)
                nowCnt = 1
                nowColor = board[row][col]
            else:
                nowCnt += 1
        maxCnt = max(maxCnt, nowCnt)

    # 열 탐색
    for col in range(N):
        nowCnt = 0
        nowColor = ""
        for row in range(N):
            if nowColor != board[row][col]:
                maxCnt = max(maxCnt, nowCnt)
                nowCnt = 1
                nowColor = board[row][col]
            else:
                nowCnt += 1
        maxCnt = max(maxCnt, nowCnt)

if __name__ == "__main__":
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(input()))

    maxCnt = 0
    findMaxCandy()

    for row in range(N):
        for col in range(N - 1):
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
            findMaxCandy()
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]

    for col in range(N):
        for row in range(N - 1):
            board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
            findMaxCandy()
            board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]

    print(maxCnt)