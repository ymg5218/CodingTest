def solution():
    for point in prob:
        for i in range(len(score)):
            if not result[point + score[i]]:
                result[point + score[i]] = True
                score.append(point + score[i])

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    prob = list(map(int, input().split()))
    _sum = sum(prob)
    result = [False for _ in range(_sum + 1)]
    result[0] = True
    score = [0]

    solution()
    print(f'#{t} {len(score)}')