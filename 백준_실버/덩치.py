# 7568

import sys
input = sys.stdin.readline

def solution():
    result = []

    for idx_1 in range(N):
        rank = 1
        for idx_2 in range(N):
            if info[idx_1][0] < info[idx_2][0] and info[idx_1][1] < info[idx_2][1]:
                rank += 1
        result.append(rank)
    
    for rank in result:
        print(rank, end=" ")

if __name__ == "__main__":
    N = int(input())
    info = []

    for _ in range(N):
        x, y = map(int, input().split())
        info.append([x, y])
        
    
    solution()

    