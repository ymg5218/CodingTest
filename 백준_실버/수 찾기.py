# 1920

N = int(input())

main_arr = list(map(int,input().split()))
dict_arr = set(main_arr)

M = int(input())

search_arr = list(map(int,input().split()))

for num in search_arr:
    if num in dict_arr:
        print(1)
    else:
        print(0)
