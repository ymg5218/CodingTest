# 15686
import sys
input = sys.stdin.readline

def back_tracking(i, cnt):
    global total_min_dis
    global visited

    if cnt == M:
        sum_dis = 0
        for h_idx in range(len(house)):
            min_dis = 10**8
            for c_idx in range(len(visited)):
                if visited[c_idx]:
                    min_dis = min(min_dis, abs(house[h_idx][0] - chicken[c_idx][0]) + abs(house[h_idx][1] - chicken[c_idx][1]))
            sum_dis += min_dis
        
        total_min_dis = min(total_min_dis, sum_dis)
        return

    for idx in range(i, len(chicken)):
        if not visited[idx]:
            visited[idx] = True
            back_tracking(idx, cnt + 1)
            visited[idx] = False
    
    return total_min_dis
    
    
def solution():
    print(back_tracking(0, 0))
    

if __name__ == "__main__":
    N, M = map(int, input().split())

    house = []
    chicken = []

    total_min_dis = 10**8

    for row in range(N):
        temp = list(map(int, input().split()))
        for col in range(N):
            if temp[col] == 1:
                house.append([row, col])
            elif temp[col] == 2:
                chicken.append([row, col])
    
    visited = [False] * (len(chicken))
    
    solution()