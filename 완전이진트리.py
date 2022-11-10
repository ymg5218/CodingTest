# 9934

# 완전 이진트리 구조의 도시

# 1. 가장 처음 트리의 루트에 있는 빌딩 앞에 서있음
# 2. 현재 빌딩의 왼쪽 자식에 있는 빌딩에 아직 들어가지 않았다면, 왼쪽 자식으로 이동
# 3. 현재 있는 노드가 왼쪽 자식 노드를 가지고 있지 않거나 왼쪽 자식에 있는 빌딩을 이미 들어갔다면,
#    현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적는다.
# 4. 현재 빌딩을 이미 들어갔다 온 상태이고, 오른쪽 자식을 가지고 있는 경우에는 오른쪽 자식으로 이동
# 5. 현재 빌딩과 왼쪽, 오른쪽 자식에 있는 빌딩을 모두 방문했다면, 부모 노드로 이동

# 중위순회를 뜻함

import math

def inorder():
    if len(arr) <= 1:
        print(str(arr[0]))
    else:
        root_index = len(arr) // 2
        print(arr[root_index]) # 루트노드 출력
        arr[root_index] = -1 # -1로 출력되었음을 알림
        parent_index = len(arr) # 부모 레벨 인덱스를 담을 변수
        for i in range(1,K-1): # 높이는 K, 루트노드는 수행했으니 횟수 - 1
            parent_index //= 2 # 부모 레벨 인덱스
            child_index = parent_index // 2 # 자식 레벨 인덱스
            nodes = ""
            while(True):
                if child_index >= len(arr):
                    break
                else:
                    nodes = nodes + str(arr[child_index]) + " "
                    arr[child_index] = -1 # -1로 출력되었음을 알림
                    child_index += parent_index
            print(nodes)
                
        leaf = ""# 리프노드 담을 배열 선언
        for val in arr:
            if val != -1:
                leaf += str(val) + " "
        print(leaf)
                

if __name__ == "__main__":
    K = int(input())
    arr = list(map(int, input().split())) # 상근이가 방문한 빌딩 순서대로 입력
    arr.insert(0,-1) # 더미값 입력
    inorder() # play 함수 실행, return된 cnt값 확인