# 6198
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    result = 0
    # 스택의 길이(특정 높이의 건물을 볼 수 있는 다른 건물들의 개수)를 담아낼 변수
    can_check = 0
    stack = []
    for _ in range(N):
        now_height = int(input())
        while stack and stack[-1] <= now_height:
            stack.pop()
            can_check -= 1
        # 현재 높이의 건물 옥상을 볼 수 있는 건물들의 개수를 result에 합산
        result += can_check
        # 해당 높이의 건물을 stack에 append
        stack.append(now_height)
        can_check += 1

    print(result)