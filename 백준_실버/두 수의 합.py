# 3273

import sys
input = sys.stdin.readline

def solution():
    cnt = 0
    
    for _ in range(n):
        find_num = x - set_arr.pop()
        if find_num in set_arr:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    n = int(input())
    
    arr = list(map(int, input().split()))

    set_arr = set(arr)

    x = int(input())

    solution()