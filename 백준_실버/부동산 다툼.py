# 20364

'''
내 예상 풀이
1. 입력값 입력받음. tree는 N의 크기 + 1만큼 선언. 0번째 인덱스는 더미
2. 각 노드가 점유당한 상태인지 확인하는 bool 형태 배열 선언. 크기는 N+1,0번째 인덱스는 더미
3. 가고 싶은 땅의 인덱스가 idx라고 가정할 때, idx //= 2를 반복하며 자식 -> 부모 순으로 루트노드까지 경로를 역추적함
4. 가장 상위레벨의 부모노드부터 다시 경로를 탐색하며, 점유당한 땅이 있다면 해당 노드를 print, idx까지 점유당한 땅을 마주하지 못했다면 0을 print 후,
    tree의 idx번째 요소를 점유당했다고 표시
'''
import sys
input = sys.stdin.readline

N,Q =map(int,input().split())

tree = [i for i in range(N+1)] # 0번째 인덱스는 더미 값
occupancy = [False] * (N+1) # 0번째 인덱스는 더미 값. 점유중인 땅의 여부를 담을 배열 occupancy
occupancy[0] = True
occupancy[1] = True # 어차피 모든 오리들은 루트노드에서 기다림

for _ in range(Q):
    goto = int(input()) # 오리가 가고싶은 땅
    idx = goto # 가고싶은 땅 번호를 일단 idx에 담아둠
    path = [] # goto까지 가는 경로를 담을 배열 (역순으로 담길 예정)
    while(1):
        if idx < 1: 
            break
        path.append(idx)
        idx //= 2 # 바텀 - 업(역추적)

    is_blocking = False # 중간에 점유당한 땅을 만났는지

    for i in range(len(path) - 2,-1,-1): # 루트노드의 다음 노드부터 탐색 -> path 중, 점유당한 땅이 있는지..
        if occupancy[path[i]] == True: 
            print(path[i])
            is_blocking = True
            break
    if is_blocking == False: # 중간에 가로막히지 않고 무사히 가고싶은 땅까지 이동했다면
        print(0) # 0 출력
        occupancy[goto] = True # 성공적으로 땅 점유!