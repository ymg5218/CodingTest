# 위로 혹은 아래로 조이스틱 움직여서 어디가 더 가까운지 탐색
def now_alpha(target):
    return min(ord(target) - ord("A"), ord("Z") - ord(target) + 1)
     

def solution(name):
    answer = 0
    length = len(name)

    # 연속된 A의 시작점 왼쪽 인덱스
    left = 0
    
    move = length - 1

    while left < length:
        # left를 한 칸씩 옮기며 탐색하니, 탐색하는 김에 상/하 조작 회수 카운트
        answer += now_alpha(name[left])
        # 연속된 A의 끝점 오른쪽 인덱스
        right = left + 1
        while right < length and name[right] == "A":
            right += 1

        # 현재 연속된 A 문자열을 피하면서, 나머지 문자들을 탐색하는 최소한의 횟수
        move = min(move, left * 2 + length - right, (length - right) * 2 + left)
        left = right

    answer += move

    return answer

if __name__ == "__main__":
    name = "AAABBBAAAA"
    print(solution(name))