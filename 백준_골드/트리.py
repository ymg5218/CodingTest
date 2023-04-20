# 1068

'''
내 예상 풀이
1. 트리를 연결리스트 형태로 입력받는다.
2. 삭제할 노드 자체를 삭제해버린다 >> tree[삭제할노드 인덱스].clear()
3. dfs로 tree를 탐색하며, 새로운 new_tree에 새로운 연결관계를 삽입한다.
3-1. 삭제한 노드를 만나지 않았다면 계속 연결관계를 new_tree에 삽입
3-2. 만약 삭제한 노드(tree[삭제한노드 인덱스]의 길이가 0임으로 판단 가능)를 만났다면, 연결관계 적시 무시하고 return
4. new_tree에서, 연결관계가 1개 뿐인 노드 == 리프노드 이므로, 조건에 맞는 리프노드의 개수를 출력
'''

def dfs(p_node,c_node):
    global tree, visited, new_tree
    if visited[c_node]:
        return
    visited[c_node] = True
    if len(tree[c_node]) == 0: # 삭제한 노드는 비어있을 것. 삭제한 노드를 만났다면?
        return # append 작업 무시하고 return
    if p_node == -1: # c_node가 루트노드면 새로운 tree의 루트노드 인덱스에 -1만 삽입
        new_tree[c_node].append(p_node)
    else:
        # 새로운 tree 배열에 새로운 연결관계 적시
        new_tree[p_node].append(c_node)
        new_tree[c_node].append(p_node)
    for v in tree[c_node]:
        if v == -1: # -1은 루트노드임을 적시해주는 역할이기에 pass
            continue
        dfs(c_node,v)

N = int(input())
tree = [[] for _ in range(N)]
visited = [False] * N
leaf_cnt = 0 # 리프노드의 개수를 담을 변수

arr = list(map(int,input().split()))

r_node = -1 # 루트노드 인덱스를 담을 배열
for i in range(N):
    v = arr[i]
    if v == -1: # 루트노드라면
        tree[i].append(v) # 해당 노드가 루트노드라는 점만 기록한다.
        r_node = i
        continue
    # 트리를 연결리스트 형태로 입력받는다.
    tree[i].append(v)
    tree[v].append(i)

d_node = int(input()) # 삭제할 노드 입력받음

# 삭제할 노드의 부모노드는 visited = True로 전환. 부모노드를 탐색하지 않도록 함.
if -1 in tree[d_node] : # 부모노드가 -1이면 루트노드임
    print(0) # 0 출력하고 종료
    exit()

tree[d_node].clear() # 삭제할 노드를 없애버림으로써 삭제할 노드의 부모노드라인 / 자식노드라인 연결 끊어버림

new_tree = [[] for _ in range(N)] # 삭제한 노드의 부모라인까지의 트리를 담을 새로운 트리배열

dfs(-1,r_node)

# 리프노드는 연결관계가 하나밖에 없다(부모 - 자식) == 해당 인덱스 부분배열의 길이는 1이다
for idx in range(N):
    if len(new_tree[idx]) == 1:
        leaf_cnt += 1
print(leaf_cnt)
