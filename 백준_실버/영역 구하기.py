# 2583

import sys
from collections import deque
input = sys.stdin.readline()


if __name__ == "__main__":
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        now_row = y1

