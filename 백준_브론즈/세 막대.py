# 14215

arr = list(map(int,input().split()))

max = max(arr)
arr.remove(max)

if arr[0] + arr[1] <= max:
    max = arr[0] + arr[1] - 1

print(arr[0] + arr[1] + max)
