# 1931
import sys
input = sys.stdin.readline

def solution():
    state.sort(key = lambda x:[x[1], x[0]])
    cnt = 1

    nowEndTime = state[0][1]

    for idx in range(1, N):
        if state[idx][0] >= nowEndTime:
            cnt += 1
            nowEndTime = state[idx][1]

    return cnt

if __name__ == "__main__":
    N = int(input())
    state = []
    for _ in range(N):
       state.append(list(map(int, input().split())))

    print(solution())
