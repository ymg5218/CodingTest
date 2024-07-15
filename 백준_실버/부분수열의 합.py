# 1182

def backTracking(nowLen, maxLen, nowNums, nowIdx):
    global result
    if maxLen == nowLen:
        if sum(nowNums) == S:
            result += 1
        return
    for i in range(nowIdx, N):
        nowNums.append(nums[i])
        backTracking(nowLen + 1, maxLen, nowNums, i + 1)
        nowNums.pop()

if __name__ == "__main__":
    N, S = map(int ,input().split())

    nums = list(map(int, input().split()))
    result = 0

    for maxLen in range(1, N + 1):
        backTracking(0, maxLen, [], 0)

    print(result)
