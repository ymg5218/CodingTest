# 던전이 최대 8개이기 때문에 백트래킹으로 모든 경우의 수를 고려해보아도 괜찮겠다고 판단.
def back_tracking(dungeons, dungeons_combi, now_length, max_length, used, k):
    global answer
    
    if now_length == max_length:
        can_explor = 0
        for min_req, cost in dungeons_combi:
            # 최소 필요 피로도 충족
            if k >= min_req:
                k -= cost
                can_explor += 1
            else:
                break
        answer = max(answer, can_explor)
        return

    for i in range(max_length):
        if not used[i]:
            used[i] = True
            dungeons_combi.append(dungeons[i])
            back_tracking(dungeons, dungeons_combi, now_length + 1, max_length, used, k)
            dungeons_combi.pop()
            used[i] = False


def solution(k, dungeons):
    global answer
    answer = 0

    used_dungeons = [False] * (len(dungeons))
    back_tracking(dungeons, [], 0, len(dungeons), used_dungeons, k)    

    return answer


if __name__ == "__main__":
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]

    print(solution(k, dungeons))