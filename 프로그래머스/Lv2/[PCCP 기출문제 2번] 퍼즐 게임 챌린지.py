def solution(diffs, times, limit):
    # diffs[i]의 최대값 : 100000
    # 내 숙련도의 최대값은 100001
    left = 1
    right = 100001

    # 퍼즐의 개수 n
    n = len(diffs)

    while left < right:
        # mid : 현재 숙련도
        mid = (left + right) // 2
        # 현재 숙련도로 소요한 시간
        now_spend_time = 0
        # 제한 시간을 넘었는지 체크
        is_timeover = False

        for idx in range(n):
            if mid >= diffs[idx]:
                now_spend_time += times[idx]
            else:
                now_spend_time += ((times[idx] + times[idx - 1]) * (diffs[idx] - mid) + times[idx])

            if limit < now_spend_time:
                is_timeover = True
                break

        if is_timeover:
            left = mid + 1
        else:
            right = mid

    return right

if __name__ == "__main__":
    diffs = [1, 328, 467, 209, 54]
    times = [2, 7, 1, 4, 3]
    limit = 1723

    print(solution(diffs, times, limit))