# 10816

if __name__ == "__main__":
    N = int(input())
    numList = list(map(int, input().split()))

    numDict = dict({})
    for idx in range(N):
        if numList[idx] not in numDict:
            numDict[numList[idx]] = 1
        else:
            numDict[numList[idx]] += 1
    
    M = int(input())
    getNumList = list(map(int, input().split()))
    
    result = []
    
    for idx in range(M):
        if getNumList[idx] in numDict:
            result.append(numDict[getNumList[idx]])
        else:
            result.append(0)
    
    for re in result:
        print(re, end=' ')