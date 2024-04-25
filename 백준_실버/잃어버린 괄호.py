# 1541
from collections import deque

def solution():
    minus_nums = deque([])
    plus_nums = deque([])
    now_num = ""
    for idx in range(len(str)):
        if str[idx] != "+" and str[idx] != "-":
            now_num += str[idx]
        elif str[idx] == "+":
            plus_nums.append(int(now_num))
            now_num = ""
        else:
            sum = int(now_num)
            while plus_nums:
                sum += plus_nums.popleft()
            minus_nums.append(sum)
            now_num = ""
    
    if now_num != "":
        plus_nums.append(int(now_num))
    # 남은 plus_nums 요소 합해서 minus_nums에 append하기
    sum = 0
    while plus_nums:
        sum += plus_nums.popleft()
    minus_nums.append(sum)

    result = minus_nums.popleft()
    
    while minus_nums:
        result -= minus_nums.popleft()
    
    print(result)


if __name__ == "__main__":
    str = input()

    solution()