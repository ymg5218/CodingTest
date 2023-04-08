# 26091

# 두 명 뽑는다 : 두 포인터
# 두 사람의 능력치 합이 최소 M -> M에 근접하게 구성하려면 최소 + 최대 >= M 일 때 가장 이상적이고 실제로 더 많은 팀 구성 가능 : 그리디

'''
내 예상 풀이
1. 입력 받음
2. 입력받은 student(학생 능력치 배열)을 오름차순으로 정렬함
3. 학생 a,b를 각각 0, N-1로 구성. 가장 능력치가 작은 학생과 가장 큰 학생과 매핑시켜놓음
4. 둘의 능력치 합이 M을 넘으면 cnt(팀 개수) + 1, a와 b의 위치도 중앙으로 한 칸 씩 땡김
4-1 둘의 능력치 합이 M을 넘지 못하면 a의 위치만 중앙으로 한 칸 땡김.(능력치가 큰 학생보다 적은 학생 버리는게 이상적임)
5. 4, 4-1 과정을 a가 b와 같거나 b보다 커질 때까지 반복하고, 마지막으로 cnt 값을 출력하면 끝
'''
import sys
input = sys.stdin.readline


N,M = map(int,input().split())

student = list(map(int,input().split()))

student.sort()
a = 0
b = N - 1
cnt = 0

while(a < b):
    if student[a] + student[b] >= M:
        cnt += 1
        a += 1
        b -= 1
    else:
        a += 1
print(cnt)