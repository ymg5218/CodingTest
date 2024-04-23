# 1389

import sys
input = sys.stdin.readline

def floyd_warshall():
    for point in range(1, N+1):
        for row in range(1, N+1):
            for col in range(1, N+1):
                relation[row][col] = min(relation[row][col], relation[row][point] + relation[point][col])
    
    min_cnt = (N + 1) * N
    min_person = -1

    for person in range(1, N + 1):
        temp = sum(relation[person]) - 6
        if min_cnt > temp:
            min_person = person
            min_cnt = temp
    
    print(min_person)
        

if __name__ == "__main__":
    N, M = map(int, input().split())

    # 관계 테이블
    # 0행, 0열은 더미 값
    relation = []
    for i in range(N+1):
        temp = []
        for j in range(N+1):
            if i == j:
                temp.append(0)
            else:
                temp.append(N+1)
        relation.append(temp)

    for _ in range(M):
        row, col = map(int, input().split())
        relation[row][col] = 1
        relation[col][row] = 1

    floyd_warshall()