# 1149

def solution():
    # 0번째 인덱스 : 마지막으로 빨간색을 칠했을 때의 최솟값
    # 1번째 인덱스 : 마지막으로 초록색을 칠했을 때의 최솟값
    # 2번째 인덱스 : 마지막으로 파란색을 칠했을 때의 최솟값
    dp = [[1000*1000 + 1, 1000*1000 + 1, 1000*1000 + 1] for _ in range(N)]
    
    dp[0][0] = red[0]
    dp[0][1] = green[0]
    dp[0][2] = blue[0]

    for idx in range(1, N):
        # ex) 빨간색을 마지막으로 칠했을 때의 최솟값 : min(dp[idx - 1][빨간색이 아닌 경우의 값] + 빨간색으로 칠하는 비용)
        for color in range(3):
            if color == 0:
                dp[idx][color] = min(dp[idx - 1][(color + 1) % 3], dp[idx - 1][(color + 2) % 3]) + red[idx]
            elif color == 1:
                dp[idx][color] = min(dp[idx - 1][(color + 1) % 3], dp[idx - 1][(color + 2) % 3]) + green[idx]
            else:
                dp[idx][color] = min(dp[idx - 1][(color + 1) % 3], dp[idx - 1][(color + 2) % 3]) + blue[idx]

    print(min(dp[-1]))

if __name__ == "__main__":
    N = int(input())

    red = []
    green = []
    blue = []

    for _ in range(N):
        _red, _green, _blue = map(int,input().split())
        red.append(_red)
        green.append(_green)
        blue.append(_blue)
    
    solution()
    