# 2805

def binary_search():
    # 최저점 : 0
    # 최고점 : 트리 중 가장 높이가 큰 트리의 높이
    low_point = 0
    high_point = max(tree)

    while low_point <= high_point:
        mid = (low_point + high_point) // 2
        
        # 이번 절단으로 얻게되는 양
        get_amount = 0

        for idx in range(N):
            cutted = tree[idx] - mid
            # 유효하게 잘렸을 때에만 합산
            if cutted > 0:
                get_amount += cutted
        
        if get_amount == M:
            return mid
            
        # 이번 절단으로 얻게되는 양이 M보다 큼
        # 너무 많이 잘랐으므로 mid를 위로 올려야함 -> low_point = mid + 1
        elif get_amount > M:
            low_point = mid + 1
        # 이번 절단으로 얻게되는 양이 M보다 적음
        # 너무 적게 잘랐으므로 mid를 아래로 내려야 함 -> high_point = mid - 1
        else:
            high_point = mid - 1
    
    return high_point

    
if __name__ == "__main__":
    N, M = map(int, input().split())

    tree = list(map(int, input().split()))

    print(binary_search())