# 1927
import heapq
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    heap = []
    N = int(input())

    for _ in range(N):
        now = int(input())
        if now == 0:
            try:
                print(heapq.heappop(heap))
            except:
                print(0)
        else:
            heapq.heappush(heap, now)