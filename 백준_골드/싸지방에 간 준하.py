# 12764
import heapq
import sys

input = sys.stdin.readline

def solution():
    computer = [0 for _ in range(N)]
    com_count = [0 for _ in range(N)]
    cnt = 0
    while use:
        start, end = heapq.heappop(use)
        for i in range(N):
            if computer[i] <= start:
                if computer[i] == 0:
                    cnt += 1
                computer[i] = end
                com_count[i] += 1
                break
        
    print(cnt)
    for re in com_count:
        if re == 0:
            break
        print(re,end=" ")
           

if __name__ == "__main__":
    N = int(input())
    
    use = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        heapq.heappush(use, temp)

    solution()
