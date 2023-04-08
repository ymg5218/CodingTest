# 23559

'''
내 예상 풀이
1. 일단 B 코너 음식 다 골랐다고 가정
2. A 코너 음식 만족도 - B 코너 음식 만족도 (만족도 간격) 순으로 정렬
3. 만족도 간격이 큰 개쩌는 A 코너 음식을 먹어주면서 4천원씩 추가 지불, 만족도는 A 코너 음식 만족도 누적으로 산정
4. 남은 X(보유한 돈)가 4000원 미만으로 떨어지거나, 모든 A vs B 비교 케이스를 수행했을 경우 반복문 종료
5. 최종 산정된 최대 만족도 출력
'''
import sys
input = sys.stdin.readline

N,X = map(int,input().split())

satis_gap = [] # A 와 B의 만족도 차이
max_value = 0 # 최대 만족도 수치 : 최종 답

for _ in range(N):
    A,B = map(int,input().split())

    # Seq 1 : 일단 B코너 음식 모두 먹는다고 가정
    X -= 1000
    max_value += B
    if A > B: # B가 A보다 싼데 맛도 좋으면, 무조건 B 먹는게 이득이니 A 만족도가 큰 경우에만 산정
        satis_gap.append(A-B)

# 만족도 차이를 기준으로 내림차순 정렬
satis_gap.sort(reverse=True)

while(X >= 4000 and len(satis_gap) > 0): # 남은 금액이 4000원보다 적거나 모든 음식을 비교할 때까지 반복문 실행
        
        X -= 4000 # B 먹기 -> A 먹기로 변경했으니, 추가금 산정
        # A 코너 만족도를 유효하게 변경 : A 코너 음식을 먹었을 때 더 만족하는 값(만족도 간격)을 기존 누적 만족도에서 더해줌.
        max_value += satis_gap[0] 
        
        del satis_gap[0] # 산정한 케이스는 삭제함

print(max_value)