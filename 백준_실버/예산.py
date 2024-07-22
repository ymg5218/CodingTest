# 2512
def binarySearch(N, requests, budget):
    left = 0
    right = budget
    # 최종적으로 출력하고자 하는 상한선 최대 값
    upperLimit = 1

    while left < right:
        # 상한선
        mid = (left + right) // 2
        nowBudget = 0
        for req in requests:
            if req <= mid:
                nowBudget += req
            else:
                nowBudget += mid

        # 현재 책정한 상한액
        if nowBudget <= budget:
            upperLimit = max(upperLimit, mid)

        # 분배했을 때, 예산 총액을 꽉 채운다면 해당 값이 최대 상한선
        if nowBudget == budget:
            return upperLimit

        # 분배했을 때, 예산 총액이 남는다면 mid를 늘려봐야 함
        elif nowBudget < budget:
            left = mid + 1

        # 분배했을 때, 예산 총액을 넘어버렸다면 mid를 줄여봐야 함
        else:
            right = mid

    return upperLimit

if __name__ == "__main__":
    N = int(input())
    requests = list(map(int, input().split()))
    budget = int(input())
    if sum(requests) <= budget:
        print(max(requests))
    else:
        print(binarySearch(N, requests, budget))
