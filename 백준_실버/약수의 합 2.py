# 17427

import math

N = int(input())

sum = 0
'''
N보다 작은 i의 모든 배수는 모두 i를 약수로 가진다
즉, i를 1부터 증가시켜, N까지 반복문을 돌려, 모든 약수를 미리 합산하여 진행하면
O(N) 시간복잡도를 지닌다.
'''
for i in range(1,N+1):
    sum += (N // i) * i

print(sum)