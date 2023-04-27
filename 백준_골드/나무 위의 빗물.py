# 17073

'''
문제가 요하는 바 : 자식노드가 있으면 자식노드 중 하나한테 물을 1씩 흘려보냄
 = 자식노드를 가지는 노드라면 결국 물의 양이 0이 될 때까지 자식노드로 물을 흘려보낼 것
 그렇다면? 최종적으로 모든 리프노드에 물의 전체 양 W가 배분되어 있을 것이다.

내 예상 풀이
1. 입력값을 입력받음. tree는 연결리스트로 받는다.
2. 리프노드가 무엇인지 확인 => 연결된 관계가 1개밖에 없다면 리프노드다.
3. 전체 물의 양 W 을 리프노드의 개수로 나누어 출력
'''

'''
 set_tree : 트리를 연결리스트로 생성 및 리턴할 메소드
 입력 값 N : 생성할 트리의 노드 개수
 리턴 값 tree : 연결리스트로 생성한 트리
'''

import sys
input = sys.stdin.readline

def set_tree(N):
    tree = [[] for _ in range(N+1)] # 0번째 인덱스는 더미
    for _ in range(N-1):
        # tree를 연결리스트 형태로 입력받음
        v1,v2 = map(int,input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)
    return tree

''' 
 get_leafcnt : 트리의 리프노드 개수를 리턴할 메소드
 입력 값 tree : 리프노드의 개수를 알고 싶은 tree
 리턴 값 leafcnt : 해당 트리의 리프노드 개수
'''
def get_leafcnt(tree):
    leafcnt = 0
    # 더미 값과 루트노드는 노드 검사에서 제외한다.
    '''
    N = 2일 경우, 1 - 2 관계가 전부. 각 연결관계는 1개임
    해당 로직대로라면 루트노드도 리프노드라고 판단해버림.
    그런 상황을 대비하여, 루트노드도 검사에서 제외한다.
    '''
    for i in range(2,len(tree)):
        if len(tree[i]) == 1:
            leafcnt += 1
    return leafcnt

if __name__ == "__main__":
    N,W = map(int,input().split())

    # 1. 트리를 입력 받음
    # 2. 해당 트리를 get_leafcnt 메소드 파라미터로 대입
    # 3. leafcnt에 해당 tree의 리프노드 개수를 받아놓음
    leafcnt = get_leafcnt(set_tree(N))

    # 4. W / leafcnt 출력
    # 루트노드만 존재한다면, leafcnt가 0이 되어 예외가 발생하지만
    # 해당 문제에선 노드가 최소 2개이기에 상관 없음.
    print(W / leafcnt)