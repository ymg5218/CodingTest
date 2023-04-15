# 5639

'''
내 예상 풀이
1. 전위순회로 탐색한 순서대로 노드를 입력받는다.
2. 노드를 이용해 이진검색트리를 구축한다.
3. 이진검색트리를 후위순회한 순서대로 출력한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 노드는 최대 10000개.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

vertex = []

# 입력이 끝날 때까지 노드를 입력 받아 vertex에 append
while(1):
    try:
        v = int(input())
        vertex.append(v)
    except:
       break
    
# 이진 검색 트리 구축 및 후위순회 메소드 내장 클래스
class BinarySearchTree(object):
    def __init__(self): # 생성자 : 트리 초기화
      self.root = None
    
    # 이진 검색 트리에 노드 삽입
    def insert(self,data):
       self.root = self._insert_value(self.root, data)
       return self.root is not None
    
    # 삽입될 노드의 값을 기존의 노드 값과 비교하여 삽입될 위치를 특정
    def _insert_value(self,node,data):
        if node is None:
          node = Node(data)
        else:
            if data <= node.data:
              node.left = self._insert_value(node.left, data)
            else:
               node.right = self._insert_value(node.right, data)
        return node

    # 구축한 이진검색트리를 후위순위로 출력하기 위한 메소드
    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.data)

        _postorder(self.root)

if __name__ == "__main__":
    bst = BinarySearchTree()
    for v in vertex:
      bst.insert(v)
    
    bst.postorder()

    

