# 2493

def solution(N):
    stack = []
    result = [0] * N

    N -= 1
    stack.append(tower[N])
    N -= 1
    
    while N >= 0:
        new_tower = tower[N]
        while True:
            if stack and stack[-1] < new_tower:
                result[tower_dict[stack[-1]]] = tower_dict[new_tower] + 1
                stack.pop()
            else:
                break
        stack.append(new_tower)
        
        N -= 1
 
    for x in result:
        print(x ,end = " ")
        
        

if __name__ == "__main__":
    N = int(input())

    tower = list(map(int, input().split()))
    
    tower_dict = {}
    for i in range(N):
        tower_dict[tower[i]] = i

    solution(N)