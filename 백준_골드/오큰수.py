# 17298

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    arr = list(map(int, input().split()))
    result = [-1] * N

    stack = []
    for idx in range(N):
        if stack:
            if stack[-1] < arr[idx]:
                _idx =  idx - 1
                while stack and stack[-1] < arr[idx]:
                    if _idx >= 0 and result[_idx] == -1:
                        stack.pop()
                        result[_idx] = arr[idx]
                    _idx -= 1
        
        stack.append(arr[idx])
    
    for n in result:
        print(n, end=" ")
                