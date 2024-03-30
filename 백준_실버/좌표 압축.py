# 18870
import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))

dict = {sorted_arr[i] : i for i in range(len(sorted_arr))}

for i in range(N): 
    print(dict[arr[i]], end=' ')