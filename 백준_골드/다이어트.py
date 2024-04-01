# 1484

def isValid(x, y):
    # x <= y
    # a - b = x 
    # a + b = y
    # 2b = y - x  => b = (y - x) // 2
    # a = x + b
    b = (y - x) / 2
    a = x + b

    # 몸무게가 0인 경우는 없음.
    if a == 0 or b == 0:
        return -1
    
    # a가 정수형으로 떨어지는 경우에만 a 를 return
    if int(a) == a:
        return int(a)
    else:
        return -1

def solution():
    arr = [i+1 for i in range(G)]
    left_point = 0
    right_point = G-1
    
    # 답을 담을 배열
    result = []

    while left_point <= right_point:
        if G % arr[left_point] == 0:
            right_point = (G // arr[left_point]) - 1
            if right_point < left_point:
                break
            
            current_weight = isValid(arr[left_point], arr[right_point])
            
            if current_weight != -1:
                result.append(current_weight)
        left_point += 1
    
    if not result:
        print(-1)
    else:
        result.sort()
        for num in result:
            print(num)



if __name__ == "__main__":
    # G = 현재 몸무게**2 - 이전 몸무게**2 => 인수 분해
    # G = (현재 몸무게 - 이전 몸무게) * (현재 몸무게 + 이전 몸무게)
    G = int(input())
    solution()

    