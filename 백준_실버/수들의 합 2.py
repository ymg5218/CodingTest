# 2003

def solution():
    # 경우의 수 누적 값
    cnt = 0
    
    l_point = 0
    r_point = 0
    sum = arr[l_point]
    
    while True:
        if sum == M:
            cnt += 1
            r_point += 1
            if r_point >= N:
                break
            sum += arr[r_point]
        elif sum > M:
            if l_point == r_point:
                l_point += 1
                r_point += 1
                if r_point >= N:
                    break
                sum = arr[l_point]
            else:
                sum -= arr[l_point]
                l_point += 1
        else:
            r_point += 1
            if r_point >= N:
                break
            sum += arr[r_point]
                
    print(cnt)

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    solution()