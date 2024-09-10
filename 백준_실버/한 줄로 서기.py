# 1138

if __name__ == "__main__":
    N = int(input())
    line = list(map(int, input().split()))

    result = []

    for idx in range(N - 1, -1, -1):
        result.insert(line[idx], idx + 1)
    
    print(*result)