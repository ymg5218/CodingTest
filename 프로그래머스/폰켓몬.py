def solution(nums):
    answer = 0
    a = set(nums)
    if len(a) >= len(nums) // 2:
        return len(nums) // 2
    else:
        return len(a)


if __name__ == "__main__":
    print(solution([3,3,3,2,2,4]))