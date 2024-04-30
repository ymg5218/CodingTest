# 1043
import sys
from collections import deque

input = sys.stdin.readline  


def solution():
    cnt = 0
    global known
    # 뒤에서 진실을 알게 된 사람이 앞의 파티에 존재할수도 있음
    # 총 M^2번 수행해야 함
    for _ in range(M):
        for party in parties:
            # 파티에 진실을 아는 사람이 있으면
            if party & known:
                # 그 파티 사람들도 진실을 알게 됨
                known = known.union(party)

    for party in parties:
        if not known & party:
            cnt += 1
        

    print(cnt)


if __name__ == "__main__":
    N, M = map(int, input().split())
    
    # 거짓말을 알고 있는 사람들 집합
    known = set(input().split()[1:])

    # 모든 파티 집합
    parties = []

    # 파티 집합
    for _ in range(M):
        parties.append(set(input().split()[1:]))
    
    solution()