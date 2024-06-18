# 1197
import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == "__main__":
    V, E = map(int, input().split())

    cost = []

    for _ in range(E):
        cost.append(list(map(int, input().split())))
    
    cost.sort(key = lambda x:x[2])
    
    parent = [i for i in range(V + 1)]

    distance = 0
    for v1, v2, c in cost:
        if find_parent(v1) != find_parent(v2):
            union_parent(v1, v2)
            distance += c
    
    print(distance)
