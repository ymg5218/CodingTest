# 위로 혹은 아래로 조이스틱 움직여서 어디가 더 가까운지 탐색
def now_alpha(target):
    return min(ord(target) - ord("A"), ord("Z") - ord(target) + 1)
     

def solution(name):
    answer = 0
    answer += now_alpha(name[0])
    length = len(name)

    longest_A = 0
    longest_point = []
    now_A_len = 0
    start = 0
    now_idx = 1
    while now_idx < length:
        answer += now_alpha(name[now_idx])
        if name[now_idx] == "A":
            if now_A_len == 0:
                start = now_idx
            now_A_len += 1

            if now_idx == length - 1:
                if longest_A < now_A_len:
                    longest_point = [start, now_idx - 1]
                    longest_A = now_A_len

        else:
            if now_A_len > 0:
                if longest_A < now_A_len:
                    longest_point = [start, now_idx - 1]
                    longest_A = now_A_len
                    now_A_len = 0

        now_idx += 1

    if longest_point:
        answer += min(length - 1, (longest_point[0] - 1) * 2 + (length - longest_point[1] - 1), ((length - longest_point[1] - 1) * 2) - 1 + longest_point[0])
    else:
        answer += (length - 1)

    return answer

if __name__ == "__main__":
    name = "AAAABBAAAA"

    print(solution(name))