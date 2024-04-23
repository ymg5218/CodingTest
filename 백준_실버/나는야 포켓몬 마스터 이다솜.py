# 1620

def solution():
    for i in range(M):
        if ord(find[i][0]) >= 65:
            print(dict_reverse[find[i]])
        else:
            print(dict[find[i]])

if __name__ == "__main__":
    N, M = map(int, input().split())

    dict = {}
    dict_reverse = {}

    for i in range(N):
        name = input()
        dict[str(i + 1)] = name
        dict_reverse[name] = str(i + 1)
    
    find = []
    for _ in range(M):
        find.append(input())
    solution()