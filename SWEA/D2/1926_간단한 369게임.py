
N = int(input())

for i in range(1, N + 1):
    num_str = str(i)
    result = ""
    search_num = ["3", "6", "9"]
    for idx in range(len(num_str)):
        if num_str[idx] in search_num:
            result += "-"
    
    if result == "":
        print(i, end=' ')
    else:
        print(result, end=' ')