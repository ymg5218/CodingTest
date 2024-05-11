# 17951
from collections import deque

def solution():
    left, right = 0, 20*(10**5) + 1
    
    result = 0
    
    while left <= right:
        mid = (left + right) // 2

        s = 0
        group = 0
        for n in score:
            s += n
            if s >= mid:
                group += 1
                s = 0
        
        if group >= K:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    print(result)
    

if __name__ == "__main__":
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    solution()