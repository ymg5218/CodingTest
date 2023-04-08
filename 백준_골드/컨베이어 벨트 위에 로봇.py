# 20055
# (올리는 위치)   1   2   3   ... N-1  N (내리는 위치)
#                2N 2N-1 2N-2 ... N+2 N+1
# 1. 올리는 위치에 로봇을 올리면, 로봇은 벨트와 함께 1칸씩 회전
# 2. 가장 먼저 벨트에 올린 로봇부터 이동하는데, 이동하려는 칸에 로봇 없어야 하고, 그 칸에 내구도가 1 이상
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
# 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료 후 return


def seq_1(belt,robot): # 1. 로봇이랑 컨베이어 벨트 이동
    global N, K 
    belt.insert(0,belt.pop(2*N-1)) # 벨트 한 칸 이동
    robot.insert(0,robot.pop(N-1)) # 로봇 한 칸 이동
    if(robot[N-1] == "True"): # 내리는 위치에 로봇이 있다면
        robot[N-1] = "False" # 로봇 내려줌
    return belt,robot

def seq_2(belt,robot): # 2. 로봇 이동하기
    global N, K
    for i in range(N-2,-1,-1): # N-2번째 벨트부터 역순으로 탐색 1번째까지만 탐색.
        if(robot[i] == "True" and belt[i + 1] > 0 and robot[i+1] != "True"):
                    # 로봇이 적재된 벨트의 다음 벨트 내구도가 0이 아니고, 로봇이 없을 때
            robot[i] = "False" # 로봇을 한칸 옮김
            robot[i+1] = "True"
            belt[i+1] -= 1 # 옮겨진 벨트는 내구도 1 감소
    if(robot[N-1] == "True"): # 내리는 위치에 로봇이 있다면
        robot[N-1] = "False" # 로봇 내려줌
    return belt,robot

def seq_3(belt,robot): # 3. 로봇 적재
    global N, K
    robot[0] = "True" # 로봇 올리는 위치는 True로 변환
    belt[0] -= 1 # 로봇 올리는 위치의 내구도는 1 감소 시킴
    return belt,robot
def is_stop(belt):
    global N,K
    if(belt.count(0) >= K):
        return True
    return False

def play(belt,robot):
    global cnt, N, K
    cnt = 0
    while(True): # belt 배열에 내구도 0인 값이 K개일 때까지 반복
        cnt += 1 # 한 사이클 돌았음
        belt, robot = seq_1(belt,robot) # 로봇, 컨베이어 벨트 한 칸 씩 회전
        belt, robot = seq_2(belt,robot) # 로봇 이동
        if(belt[0] > 0 and robot[0] != "True"): # 올리는 위치의 내구도가 0이 아니거나 로봇이 없으면
             belt,robot = seq_3(belt,robot) # 로봇 적재
        if is_stop(belt):
            break
        
    print(cnt)


if __name__ == "__main__":
    N, K = map(int, input().split()) # N,K 값 받아옴
    belt = list(map(int, input().split())) # 벨트 내구도 배열 값 받아옴
    robot = []
    for i in range(0,N): # 로봇의 현재 위치 배열 선언 및 False로 초기화
        robot.append("False")
    
    play(belt,robot) # play 함수 실행, return된 cnt값 확인