# 1764

N, M = map(int, input().split())

not_listen = {}
not_see = {}

for _ in range(N):
    not_listen[input()] = True

for _ in range(M):
    not_see[input()] = True

result = []

for compair in not_listen:
    if compair in not_see:
        result.append(compair)

print(len(result))
result.sort()
for re in result:
    print(re)