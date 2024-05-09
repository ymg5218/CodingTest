# 2108
import sys
input = sys.stdin.readline

N = int(input())
arr = []
dict = {}
total_sum = 0
arr_length = 0
for _ in range(N):
    n = int(input())
    arr.append(n)
    total_sum += n
    arr_length += 1
    if n not in dict:
        dict[n] = 1
    else:
        dict[n] += 1

sorted_dict = sorted(dict.items(), key=lambda x:(x[1], x[0]))

arr.sort()

print(round(total_sum / N))

print(arr[N//2])

max_arr = []
max_cnt = sorted_dict[-1][1]
for i in range(len(sorted_dict) - 1, -1, -1):
    if sorted_dict[i][1] == max_cnt:
        max_arr.append(sorted_dict[i][0])
    else:
        break
if len(max_arr) == 1:
    print(max_arr[0])
else:
    print(max_arr[-2])

if arr_length != 1:
    print(arr[-1] - arr[0])
else:
    print(0)
