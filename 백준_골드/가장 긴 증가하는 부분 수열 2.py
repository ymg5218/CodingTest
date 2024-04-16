# 12015

def binary_search(lis, start, end, target):
    # lis[T - 1] < target <= lis[T] 위치를 만족하는 인덱스 T를 찾아야 한다. 그 위치가 치환할 수 있는 위치 change_idx
    while start < end: 
        mid = (start + end) // 2
        if target > lis[mid]:
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
            change_idx = binary_search(lis, 0, lis_len, A[idx])
            lis[change_idx] = A[idx]
    
    print(len(lis))
            
            

if __name__ == "__main__":
    N = int(input())

    A = list(map(int, input().split()))

    solution()