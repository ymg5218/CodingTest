# 23351

# N개의 화분에 캣닢 심어둠
# 각 화분은 K만큼의 수분을 머금고 있음
# 매일 일어나는 일
# 1. 연속된 A개의 화분에 물을 줌. 물을 준 화분의 수분은 B만큼씩 증가
# 2. 모든 화분의 수분이 1씩 감소
# 3. 수분이 0이 된 화분에 있는 캣닢은 죽음
# 모든 캣닢이 살아 있는 기간이 최대한 길어지도록 물을 줄 때, 첫 캣닢이 죽는 날짜를 출력. 첫 날은 1일

def step_1(): # 연속된 A개의 화분에 물을 각 B만큼 줌
    global day
    day += 1 # 새로운 하루 시작!
    min_pot = pot.index(min(pot)) # 가장 최소값 인덱스를 지정
    for i in range(0,A):  # 연속된 A개의 화분에 물을 줌
        pot[(min_pot + i) % N] += B # B만큼 물을 줌
       
        # 인덱스 넘어가면 곤란하니 나머지값 연산을 이용


def step_2(): # 모든 화분의 수분 1씩 감소
    global day
    for i in range(0,N):
        pot[i] -= 1
    
def step_3(): 
    if 0 in pot: # 캣닢 하나라도 죽었으면
        return True # True 반환
    else: 
        return False

if __name__ == '__main__':
    N, K, A, B = map(int, input().split())
    # N : 화분의 개수
    # K : 각 화분이 초기에 머금고 있는 수분 양
    # A : 하루에 한 번 물을 주는 화분의 개수
    # B : 물을 준 화분의 수분 양이 증가하는 양

    day = 0 
    pot = [] # 화분 현재 상태 배열
    for i in range(0,N):
        pot.append(K) # 초기 상태 기입
    while(1): # 죽은 캣닢 없을때까지 반복
        step_1()
        step_2()
        if step_3() == True : # 만약 캣닢이 하나라도 죽었다면
            print(day) # 캣닢이 죽은 날 출력
            break