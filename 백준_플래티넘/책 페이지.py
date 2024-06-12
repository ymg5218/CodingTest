# 1019

def solution():
    result = [0 for _ in range(10)]

    # 자리수 알아내기
    digit = len(N) - 1

    '''
    자리수보다 한 단계 낮은 단계는 0 ~ 999...99가 모두 존재할 것이다.
    자리수를 줄여가며 작은 문제로 계속 쪼개며 수학적으로 접근할 것
    '''
    for now in N:
        # 현재 자리수의 숫자보다 작은 수들의 경우부터 모두 연산함
        for i in range(int(now)):
            result[i] += 10**digit
            if digit >= 1:
                for j in range(10):
                    result[j] += 10**(digit - 1) * digit
        # 0이 가장 앞자리로 오는 경우는 존재하지 않으니 빼준다.
        result[0] -= 10**digit

        # 만약 자리수가 10^0의 자리가 아니라면
        if digit == len(N) - 1:
            result[int(now)]+=(int(''.join(N[-digit:]))+1)
        # 현재 자리수가 10^0이라면 그냥 자기자신이 1의 자리로 오는 한 가지 경우밖에 없으니 1 더함
        elif digit > 0:
            result[int(now)]+=(10**digit)
        else:
            result[int(now)]+=1

        digit -= 1


    print(*result)

if __name__ == "__main__":
    N = input()

    solution()