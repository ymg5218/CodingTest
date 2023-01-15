# 1991

N = int(input())

graph = {} # 딕셔너리 사용

for _ in range(N):
    root,left,right = input().strip().split() # 루트,왼쪽 자식 노드, 오른쪽 자식 노드
    graph[root] = [left,right] # root를 key값으로, left,right를 value 값으로

def preorder(root): # 전위 순회 : root -> left -> right
    if root != '.': # . 는 없는 노드임
        print(root, end='') # root
        preorder(graph[root][0]) # left
        preorder(graph[root][1]) # right
 
 
def inorder(root): # 중위 순회 : left -> root -> right
    if root != '.': # . 는 없는 노드임
        inorder(graph[root][0]) # left
        print(root, end='') # root
        inorder(graph[root][1]) # right
 
 
def postorder(root): # 후위 순회 : left -> right -> root
    if root != '.': # . 는 없는 노드임
        postorder(graph[root][0]) # left
        postorder(graph[root][1]) # right
        print(root, end='') # root
 
 
preorder('A') # 트리의 루트는 A
print()
inorder('A')
print()
postorder('A')