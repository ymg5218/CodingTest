# 1181

import sys

input = sys.stdin.readline

N = int(input())

dict = {}

for _ in range(N):
    s = input().strip()
    if s not in dict:
        dict[s] = len(s)

sorted_dict = sorted(dict.items(), key= lambda x:(x[1], x[0]))

for result in sorted_dict:
    print(result[0])