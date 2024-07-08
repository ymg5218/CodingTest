# 1786
def createTable(P):
    length = len(P)
    table = [0 for _ in range(length)]

    pidx = 0

    for idx in range(1, length):
        while pidx > 0 and P[idx] != P[pidx]:
            pidx = table[pidx - 1]

        if P[idx] == P[pidx]:
            pidx += 1
            table[idx] = pidx

    return table

def KMP(T, P):
    table = createTable(P)

    P_length = len(P)

    matchingStartPoint = []
    matchingCount = 0

    compair_idx = 0
    idx = 0

    while idx < len(T):
        if T[idx] == P[compair_idx]:
            idx += 1
            compair_idx += 1
        else:
            if compair_idx != 0:
                compair_idx = table[compair_idx - 1]
            else:
                idx += 1

        if compair_idx == P_length:
            matchingCount += 1
            matchingStartPoint.append(idx - P_length + 1)
            compair_idx = table[compair_idx - 1]


    print(matchingCount)
    print(*matchingStartPoint)



if __name__ == "__main__":
    T = input()
    P = input()

    KMP(T, P)