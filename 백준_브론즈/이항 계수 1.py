# 11050

N, K = map(int, input().split())

factorial = [1]

for i in range(1, 11):
    factorial.append(factorial[-1] * i)

print(factorial[N] // (factorial[K] * factorial[N - K]))