# 1406
import sys

def solution():
    for i in range(N):
        if command[i][0] == "P":
            s1.append(command[i][1])

        elif command[i][0] == "L":
            if s1:
                s2.append(s1.pop())
        elif command[i][0] == "D":
            if s2:
                s1.append(s2.pop())
        else:
            if s1:
                s1.pop()



if __name__ == "__main__":
    s1 = list(sys.stdin.readline().rstrip())
    s2 = []
    N = int(input())
    command = []
    for _ in range(N):
        command.append(list(map(str, sys.stdin.readline().rstrip().split())))

    solution()



    s1.extend(reversed(s2))
    print("".join(s1))

