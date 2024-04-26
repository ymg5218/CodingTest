
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    result = []

    for i in range(N):
        temp = []
        for num in range(i + 1):
            if num == 0 or num == i:
                temp.append(1)
            else:
                temp.append(result[i - 1][num - 1] + result[i - 1][num])
        result.append(temp)

    print(f'#{test_case}')
    for row in result:
        for re in row:
            print(re, end=" ")
        print()