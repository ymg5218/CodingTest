# 24230

'''
예상 풀이 과정
1. 입력 받음. 트리는 연결리스트 형태로 받는다.
2. dfs를 통해 부모와 자식의 색이 다르면, cnt를 1증가
3. dfs가 끝났을 때, cnt 값을 출력
'''
import sys
sys.setrecursionlimit(200000) # 최대 반복 횟수 : N = 200,000
input = sys.stdin.readline

def dfs(p_node,c_node): # 매개변수 : 부모노드, 자식노드
    global tree
    global visited
    global cnt

    visited[c_node] = True # 방문한 노드 기록
    '''
    부모 노드의 색과 자식 노드의 색이 다르면 색을 1회 더 입혔다는 의미
    ex) p_node = 1, c_node = 2
    1. p_node를 1로 칠하면 c_node는 자연스럽게 1로 칠해짐
    2. c_node가 2로 칠해지는 행위가 한 번 더 이루어 졌기에, c_node는 p_node와 다른 2가 가능
    '''
    if color[p_node] != color[c_node]:
        cnt += 1
    # 자식 노드 방문
    for i in tree[c_node]:
        if visited[i] == False:
            dfs(c_node,i)

if __name__ == "__main__":
    N = int(input()) # 정점 개수

    cnt = 0 # 총 색칠하는 횟수

    # tree 선언. 0번째 인덱스는 더미 값
    tree = [[] for _ in range(N + 1)]
    
    # 노드 방문 여부 판단
    # 0 : 방문 안함
    # 1 :방문 함
    # 0번째 인덱스는 더미 값
    visited = [False] * (N+1)

    #각 정점의 색 입력받기. 0번째 인덱스는 더미 값
    color = list(map(int,input().split()))
    color.insert(0,0)

    # 각 정점의 연결관계를 연결리스트로 표현
    for _ in range(N-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    # 초기 p_node : 0, c_node : 1
    dfs(0,1)
    print(cnt)