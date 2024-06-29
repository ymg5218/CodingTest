# 15649

def back_tracking(arr, now_length, used_num):
    if now_length == M:
        print(*arr)
        return
    
    for idx in range(1, N + 1):
        if not used_num[idx]:
            arr.append(idx)
            used_num[idx]= True
            back_tracking(arr, now_length + 1, used_num)
            arr.pop()
            used_num[idx] = False
    
    

if __name__ == "__main__":
    N, M = map(int, input().split())

    # 0번째 인덱스는 더미 인덱스
    nums = [i + 1 for i in range(N + 1)]
    
    used_num = [False] * (N + 1)

    back_tracking([], 0, used_num)

    