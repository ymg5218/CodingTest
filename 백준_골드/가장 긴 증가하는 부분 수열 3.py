# 12738
import sys
input = sys.stdin.readline

def binary_search(lis, start, end, target):
    change_idx = -1

    while start < end:
        mid = (start + end) // 2

        if lis[mid] < target:
            start = mid + 1
        else:
            end = mid

    change_idx = end
    return change_idx

def solution():
    lis = []
    lis_len = 0

    for idx in range(N):
        if not lis or lis[-1] < A[idx]:
            lis.append(A[idx])
            lis_len += 1
        else:
            change_idx = binary_search(lis, 0, lis_len - 1, A[idx])
            lis[change_idx] = A[idx]
    
    print(lis_len)

if __name__ == "__main__":
    N = int(input())

    A = list(map(int, input().split()))

    solution()