# 10809

s = input()

arr = [-1 for _ in range(26)]

for i in range(len(s)):
    if arr[ord(s[i]) - 97] == -1:
        arr[ord(s[i]) - 97] = i
    
for idx in range(len(arr)):
    print(arr[idx], end=" ")