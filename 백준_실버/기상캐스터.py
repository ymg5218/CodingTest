def solution():
    for row in range(H):
        now_row = []
        for col in range(W):
            if weather[row][col] == "c":
                now_row.append(0)
            elif col > 0 and now_row[-1] != -1:
                now_row.append(now_row[-1] + 1)
            else:
                now_row.append(-1)
        print(*now_row)

if __name__ == "__main__":
    H, W = map(int, input().split())
    weather = []
    for _ in range(H):
        weather.append(list(input()))

    solution()
    