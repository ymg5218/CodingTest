# 1715

import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heappush(heap,int(input()))

if N == 1:
    print(heappop(heap))
    exit()

sum = heappop(heap) + heappop(heap)
heappush(heap,sum)
while(len(heap) > 2):
    temp = heappop(heap) + heappop(heap)
    sum += temp
    heappush(heap,temp)
if N != 2:  
    sum += (heappop(heap) + heappop(heap))
print(sum)

    