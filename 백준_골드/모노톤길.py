# 11067
from collections import deque
import sys
input = sys.stdin.readline

def solution():
    while cafe:
        now = cafe.popleft()
        if cafe and cafe[0][0] == now[0]:
            temp = deque([])
            temp.append(now)
            while cafe and cafe[0][0] == now[0]:
                temp.append(cafe.popleft())
            if not seq:
                if temp[0] == [0, 0]:
                    while temp:
                        seq.append(temp.popleft())
                else:
                    while temp:
                        seq.append(temp.pop())
            elif seq[-1][1] == temp[-1][1]:
                while temp:
                    seq.append(temp.pop())
            else:
                while temp:
                    seq.append(temp.popleft())
        else:
            seq.append(now)


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        cafe_cnt = int(input())
        _cafe = []
        for _ in range(cafe_cnt):
            _cafe.append(list(map(int, input().split())))

        cafe = deque(sorted(_cafe, key= lambda x:(x[0], x[1])))

        find = list(map(int, input().split()))

        seq = []

        solution()

        for i in range(1, find[0] + 1):
            re = seq[find[i] - 1]
            print(f'{re[0]} {re[1]}')