# 1546

N = int(input())

score = list(map(int,input().split()))

def new_score(_score):
    return (_score / max(score)) * 100

def new_aver():
    total = 0
    for i in range(N):
        total += new_score(score[i])
    print(total / N) 

new_aver()