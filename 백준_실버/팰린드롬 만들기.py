# 1213

from collections import deque

def isValid(s):
    global length
    start = 0
    end = length - 1

    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True

def back_tracking(now_length, now_name):
    global re_name
    global length

    if now_length == length:
        if now_name[0] == now_name[-1]:
            temp = ""
            for x in now_name:
                temp += x
            if temp < re_name:
                if isValid(now_name):
                    re_name = temp
                return
            elif re_name == "I'm Sorry Hansoo":
                if isValid(now_name):
                    re_name = temp
                return
            
    for _ in range(length - now_length):
        now_name.append(name.popleft())
        back_tracking(now_length + 1, now_name)
        name.append(now_name.pop())


if __name__ == "__main__":
    name = deque(list(input()))

    length = len(name)
    re_name = "I'm Sorry Hansoo"
    back_tracking(0, [])

    print(re_name)