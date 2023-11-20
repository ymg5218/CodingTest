# https://www.acmicpc.net/contest/problem/1149/1

def suffix(str):
    length = len(str)
    for idx in range(length):
        temp = str[idx:]
        if temp in suffix_dict:
            suffix_dict[temp] += 1
        else:
            suffix_dict[temp] = 1

def solution():
    cnt = 0
    for suffix in suffix_dict:
        if suffix_dict[suffix] % 2 == 1:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    N = int(input())

    suffix_dict = {}

    for _ in range(N):
        suffix(input())
    
    solution()
    
