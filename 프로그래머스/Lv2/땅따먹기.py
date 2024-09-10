def solution(land):

    length = len(land)

    now_row = 1
    dp = [[0 for _ in range(4)] for _ in range(length)]
    dp[0] = land[0][:]

    while now_row < len(land):
        for now_col in range(4):

            max_value = 0

            for last_col in range(4):

                if now_col == last_col:
                    continue

                max_value = max(max_value, dp[now_row - 1][last_col] + land[now_row][now_col])
            
            dp[now_row][now_col] = max_value

        now_row += 1
    
    return max(dp[-1])

if __name__ == "__main__":
    land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
    print(solution(land))