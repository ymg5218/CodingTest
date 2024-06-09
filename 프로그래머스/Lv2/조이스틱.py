# 오른쪽으로 이동 후, 가까운 위치 찾으며 탐색
def movecase_1(arr, incorr_cnt):
    cnt = 0
    # 현재 탐색 인덱스
    now_idx = 0
    # 오른쪽으로 이동해볼 때, 가장 가까운 초기 위치 탐색
    for i in range(1, len(arr)):
        if arr[i] != 0:
            # 찾았다면 now_idx 갱신
            # 해당 위치는 수정을 해주었음을 표기
            now_idx = i
            cnt += i
            arr[i] = 0
            incorr_cnt -= 1
            break

    cnt += find_minimum(arr, now_idx, incorr_cnt)

    return cnt

    

# 왼쪽으로 이동 후, 가까운 위치 찾으며 탐색
def movecase_2(arr, incorr_cnt):
    # 가장끝으로 이동하고 시작하므로 1로 시작
    cnt = 1
    # 현재 탐색 인덱스
    now_idx = 0
    # 왼쪽으로 이동해볼 때, 가장 가까운 초기 위치 탐색
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            # 찾았다면 now_idx 갱신
            # 해당 위치는 수정을 해주었음을 표기
            now_idx = i
            cnt += i
            arr[i] = 0
            incorr_cnt -= 1
            break

    cnt += find_minimum(arr, now_idx, incorr_cnt)

    return cnt

def find_minimum(arr, start_idx, incorr_cnt):
    length = len(arr)
    now_idx = start_idx

    cnt = 0

    while incorr_cnt > 0:
        go_left = now_idx
        left_cnt = 0
        # 좌로 이동
        while True:
            if arr[go_left] != 0:
                break
            go_left = (go_left - 1 + length) % length
            left_cnt += 1

        go_right = now_idx
        right_cnt = 0
        # 우로 이동
        while True:
            if arr[go_right] != 0:
                break
            go_right += 1
            go_right %= len(arr)
            right_cnt += 1
        
        # 더 움직인 횟수가 적은 방향으로 결정
        if left_cnt <= right_cnt:
            now_idx = go_left
            cnt += left_cnt
            
        else:
            now_idx = go_right
            cnt += right_cnt
        arr[now_idx] = 0
    
    return cnt
            

# 위로 혹은 아래로 조이스틱 움직여서 어디가 더 가까운지 탐색
def now_alpha(target):
    return min(abs(ord("A") - ord(target)), abs(ord("Z") - ord(target) + 1))
     

def solution(name):
    answer = 0
    length = len(name)

    change_arr = []
    incorrect_cnt = 0
    for i in range(length):
        change_cnt = now_alpha(name[i])
        if change_cnt > 0:
            incorrect_cnt += 1
        answer += change_cnt
        change_arr.append(change_cnt)

    answer += min(movecase_1(change_arr[:], incorrect_cnt), movecase_2(change_arr[:], incorrect_cnt))

    return answer

if __name__ == "__main__":
    name = "BAABBAAA"

    print(solution(name))