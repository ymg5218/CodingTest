# 14003
import sys
input = sys.stdin.readline

def binary_search(lis, start, end, target):
    change_idx = -1

    while start < end:
        mid = (start + end) // 2

        if lis[mid][0] < target:
            start = mid + 1
        else:
            end = mid

    change_idx = end
    return change_idx

def solution():
    lis = []
    lis_len = 0
    lis_detailed = []
    order = 1

    for idx in range(N):
        if not lis or lis[-1][0] < A[idx]:
            lis.append([A[idx], order])
            lis_len += 1
            lis_detailed.append([A[idx], order])
            order += 1
        else:
            change_idx = binary_search(lis, 0, lis_len - 1, A[idx])
            lis[change_idx][0] = A[idx]
            lis_detailed.append([A[idx], lis[change_idx][1]])
    
    print(lis_len)
    order -= 1

    result_LIS = []

    for i in range(N-1, -1, -1):
        if order <= 0:
            break
        if lis_detailed[i][1] == order:
            result_LIS.append(lis_detailed[i][0])
            order -= 1
    
    for _ in range(lis_len):
        print(result_LIS.pop(), end=" ")
    

if __name__ == "__main__":
    N = int(input())

    A = list(map(int, input().split()))

    solution()