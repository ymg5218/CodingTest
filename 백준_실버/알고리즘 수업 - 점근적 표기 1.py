# 24313

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}

if c * n0 >= a1 * n0 + a0 and a1 <= c:
    print(1)
else:
    print(0)