# 1965


def solution() -> int:
    # 현재 박스의 조합을 담을 배열
    dp = [1 for _ in range(n)]

    for idx_1 in range(n):
        for idx_2 in range(idx_1):
            if box[idx_2] < box[idx_1]:
                dp[idx_1] = max(dp[idx_1], dp[idx_2] + 1)
        

    return max(dp)


if __name__ == "__main__":
    n = int(input())

    box = list(map(int, input().split()))

    print(solution())