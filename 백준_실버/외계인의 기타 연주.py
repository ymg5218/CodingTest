# 2841
import sys
input = sys.stdin.readline

def solution():
    cnt = 0
    # 각 음계의 어느 프렛에 손가락이 올라가있는지 확인하기 위한 6개의 스택 선언
    # 0번째 스택은 더미 스택
    stack = [[] for _ in range(7)]

    for idx in range(N):
        now_level, now_fret = melody[idx]
        if not stack[now_level] or stack[now_level][-1] < now_fret:
            stack[now_level].append(now_fret)
            cnt += 1
        else:
            while stack[now_level] and stack[now_level][-1] > now_fret:
                stack[now_level].pop()
                cnt += 1
            if not stack[now_level] or stack[now_level][-1] < now_fret:
                stack[now_level].append(now_fret)
                cnt += 1

    return cnt


if __name__ == "__main__":
    N, P = map(int, input().split())
    melody = []
    for _ in range(N):
        melody.append(list(map(int, input().split())))

    print(solution())