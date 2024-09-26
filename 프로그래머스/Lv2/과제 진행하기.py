def solution(plans):
    complete = []
    
    # 과제를 진행하다 끝내지 못한 과제들의 정보를 담아낼 2차원 배열
    # [idx][0] = 과제 이름
    # [idx][1] = 해당 과제를 끝내는데 남은 시간
    not_complete = []

    plans.sort(key=lambda x:x[1])

    # 데이터 가공 -> 시작 시간을 분 단위로 통일, playtime은 과제를 끝내기까지 남은 시간으로 취급
    start_hour, start_min = map(int, plans[0][1].split(":"))
    plans[0][1] = 60 * start_hour + start_min
    plans[0][2] = int(plans[0][2])
    for idx in range(1, len(plans)):
        start_hour, start_min = map(int, plans[idx][1].split(":"))
        plans[idx][1] = 60 * start_hour + start_min
        plans[idx][2] = int(plans[idx][2])

        left_time = 0
        # 과제를 시작했을 때, 다음 순번의 과제를 시작하기 전까지 끝낼 수 있는 경우
        if plans[idx - 1][1] + plans[idx - 1][2] <= plans[idx][1]:
            complete.append(plans[idx - 1][0])
            # 이전 과제를 끝내고 다음 과제를 시작하는 사이의 남는 시간을 left_time에 저장
            left_time += plans[idx][1] - (plans[idx - 1][1] + plans[idx - 1][2])
            # 여유 시간이 존재하면 반복문 수행
            while left_time > 0:
                if not not_complete:
                    break
                # 여유 시간동안 재시작할 과제를 다 끝내지 못한 경우
                if not_complete[-1][1] > left_time:
                    not_complete[-1][1] -= left_time
                    break
                # 여유 시간동안 재시작할 과제를 다 끝낼 수 있는 경우
                else:
                    # 남은 여유 시간에서 재시작했던 과제를 수행한 시간 만큼 차감하여 다른 과제를 재시작
                    left_time -= not_complete[-1][1]
                    complete.append(not_complete.pop()[0])
        
        # 과제를 시작했을 때, 다음 순번의 과제를 시작하기 전까지 못 끝내게 되는 경우
        else:
            not_complete.append([plans[idx - 1][0], plans[idx - 1][2] - (plans[idx][1] - plans[idx - 1][1])])
    
    # plans의 마지막에 있는 과제는 시작하면 끝까지 진행하게 됨
    complete.append(plans[-1][0])
    
    # 아직 못 끝낸 과제들 중에선, 최근에 끝낸 과제부터 재시작해야함
    while not_complete:
        complete.append(not_complete.pop()[0])

    return complete

if __name__ == "__main__":
    plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
    print(solution(plans))