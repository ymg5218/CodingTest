# 1946

import sys
input = sys.stdin.readline

def solution():
    cnt = 1
    compair_score = sorted_apps[0][1]
    for idx in range(1, N):
        if sorted_apps[idx][1] < compair_score:
            cnt += 1
            compair_score = sorted_apps[idx][1]
        
    print(cnt)


if __name__ == "__main__":
    T = int(input())    
    apps = []
    for _ in range(T):
        apps.clear()
        N = int(input())
        for _ in range(N):
            a, b = map(int, input().split())
            apps.append([a,b])
        sorted_apps = sorted(apps, key= lambda x: x[0])
        
        solution()