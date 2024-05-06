def solution():
    

T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int,input().split())

    dp = [0 for _ in range(L)]

    ingred = []
    for _ in range(N):
        ingred.append(list(map(int, input().split())))
    ingred.sort(key=lambda x:x[1])
    print(ingred)
    solution()

    print(f'#{test_case} ')