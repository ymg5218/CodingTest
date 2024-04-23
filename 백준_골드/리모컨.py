# 1107

def find_nearest_num():
    min_gap = 10**9
    nearest_num = -1
    now_num = 0
    
    while True:
        now_num_str = str(now_num)
        # 유효한 버튼으로 조합 가능 숫자인지 확인
        is_valid = True
        for i in range(len(now_num_str)):
            if int(now_num_str[i]) not in btn:
                now_num += 1
                is_valid = False
                break
        
        if is_valid:
            # 최소 차이보다 더 작은 차이를 찾았다면 nearest_num 갱신
            if abs(now_num - N) < min_gap:
                min_gap = abs(now_num - N)
                nearest_num = now_num
            # 차이가 벌어지기 시작했다면 그 이후 숫자는 탐색할 필요없음 -> 탐색 종료
            else:
                break

            now_num += 1
        
    return nearest_num

def solution():
    nearest_num = find_nearest_num()

    cnt = 0
    now_ch = 100

    cnt += len(str(nearest_num))
    cnt += abs(N - nearest_num)

    if abs(N - now_ch) < cnt:
        return abs(N - now_ch)
    else:
        return cnt


if __name__ == "__main__":
    N = int(input())
    
    M = int(input())
    
    btn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if M != 0:
        broken = list(map(int, input().split()))
        for b_btn in broken:
            btn.remove(b_btn)
    if not btn:
        print(abs(100 - N))
    elif btn[-1] == 0:
        print(min(abs(100 - N), N + 1))
    else:
        print(solution())