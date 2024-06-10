# 11723
import sys
input = sys.stdin.readline

def add(dict, x):
    dict[x] = 1
    return dict

def check(dict, x):
    return dict[x]

def remove(dict, x):
    dict[x] = 0
    return dict

def toggle(dict, x):
    if dict[x] == 1:
        dict[x] = 0
    else:
        dict[x] = 1
    return dict

def all():
    return {
        "1" : 1, "2" : 1, "3" : 1, "4" : 1, "5" : 1,
        "6" : 1, "7" : 1, "8" : 1, "9" : 1, "10" : 1,
        "11" : 1, "12" : 1, "13" : 1, "14" : 1, "15" : 1,
        "16" : 1, "17" : 1, "18" : 1, "19" : 1, "20" : 1
    }

def empty():
    return {
        "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
        "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
        "11": 0, "12": 0, "13": 0, "14": 0, "15": 0,
        "16": 0, "17": 0, "18": 0, "19": 0, "20": 0
    }

def main():
    M = int(input())

    dict = {
        "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
        "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
        "11": 0, "12": 0, "13": 0, "14": 0, "15": 0,
        "16": 0, "17": 0, "18": 0, "19": 0, "20": 0
    }

    for _ in range(M):
        op = list(map(str, input().split()))
        if op[0] == "add":
            dict = add(dict, op[1])
        elif op[0] == "check":
            print(check(dict, op[1]))
        elif op[0] == "remove":
            dict = remove(dict, op[1])
        elif op[0] == "toggle":
            dict = toggle(dict, op[1])
        elif op[0] == "all":
            dict = all()
        else:
            dict = empty()

if __name__ == "__main__":
    main()