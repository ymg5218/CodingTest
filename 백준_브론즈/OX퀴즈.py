# 8958

T = int(input())
for _ in range(T):
    str = input()
    total_score = 0
    now_score = 0
    for i in range(len(str)):
        if str[i] == "O":
            now_score += 1
            total_score += now_score
        else:
            now_score = 0
    
    print(total_score)