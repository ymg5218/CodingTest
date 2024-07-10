# 14889

def makeTeam(nowLen, nowIdx):
    if nowLen == maxLen:
        setAbilityGap()
        return

    for idx in range(nowIdx, N):
        if not startTeam[idx]:
            startTeam[idx] = True
            makeTeam(nowLen + 1, idx)
            startTeam[idx] = False

def setAbilityGap():
    global abilityGap

    startTeamAbility = 0
    linkTeamAbility = 0

    for x in range(N):
        for y in range(x + 1, N):
            if startTeam[x] and startTeam[y]:
                startTeamAbility += (table[x][y] + table[y][x])
            elif not startTeam[x] and not startTeam[y]:
                linkTeamAbility += (table[x][y] + table[y][x])

    abilityGap = min(abilityGap, abs(startTeamAbility - linkTeamAbility))


if __name__ == "__main__":
    N = int(input())
    table = []
    for i in range(N):
        table.append(list(map(int, input().split())))

    maxLen = N // 2
    people = [i for i in range(N)]
    startTeam = [False for _ in range(N)]
    startTeam[0] = True

    # 능력치 최소값 1, 두 사람이 같은 팀일 때 최소값 2
    # 능력치 최대값 100, 두 사람이 같은 팀일 때 최대값 200
    # 팀 최대 인원 10명 -> 능력치 차이 최대값 200 * 10 - 2 * 10
    abilityGap = 1981

    cnt = 0
    makeTeam(1, 1)

    print(abilityGap)