# 14888
import sys
input = sys.stdin.readline

def backTracking(nowOpsLength, nowResult, nowIdx):
    global maxResult, minResult
    if nowOpsLength == N - 1:
        maxResult = max(maxResult, nowResult)
        minResult = min(minResult, nowResult)
        return

    for i in range(N - 1):
        if not usedOps[i]:
            usedOps[i] = True
            if ops[i] == "+":
                backTracking(nowOpsLength + 1, nowResult + numList[nowIdx], nowIdx + 1)
            elif ops[i] == "-":
                backTracking(nowOpsLength + 1, nowResult - numList[nowIdx], nowIdx + 1)
            elif ops[i] == "*":
                backTracking(nowOpsLength + 1, nowResult * numList[nowIdx], nowIdx + 1)
            else:
                if nowResult >= 0:
                    backTracking(nowOpsLength + 1, nowResult // numList[nowIdx], nowIdx + 1)
                else:
                    backTracking(nowOpsLength + 1, (nowResult * -1) // numList[nowIdx] * -1, nowIdx + 1)
            usedOps[i] = False


if __name__ == "__main__":
    N = int(input())
    numList = list(map(int, input().split()))
    _ops = list(map(int, input().split()))

    ops = []
    usedOps = []
    for idx in range(4):
        while _ops[idx] > 0:
            if idx == 0:
                ops.append("+")
            elif idx == 1:
                ops.append("-")
            elif idx == 2:
                ops.append("*")
            else:
                ops.append("/")
            _ops[idx] -= 1
            usedOps.append(False)

    maxResult = -10**9 - 1
    minResult = 10**9 + 1

    backTracking(0, numList[0], 1)

    print(maxResult)
    print(minResult)

