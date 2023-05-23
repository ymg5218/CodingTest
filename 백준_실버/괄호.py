# 9012

def solution(VPS):
    cnt = 0
    for idx in range(len(VPS)):
        if VPS[idx] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return "NO"
    if cnt == 0:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(solution(input()))
    