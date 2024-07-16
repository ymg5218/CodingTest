from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    bridge_queue = deque()
    # 현재 다리 위에 존재하는 트럭의 개수
    nowTruckOnBridge = 0
    # 현재 다리가 지탱할 수 있는 무게
    nowWeight = weight
    complete = []

    time = 0

    '''
    1. 다리를 지날 수 있는 트럭이 있으면 다리를 지나게 함
    2. 다리에 트럭을 올릴 수 있으면 올림
    '''
    while truck_queue or bridge_queue:
        time += 1
        # 다리를 지날 수 있는 트럭이 있으면 다리를 지나게 함
        if bridge_queue and time == bridge_queue[0][1]:
            complete.append(bridge_queue.popleft())
            nowWeight += complete[-1][0]
            nowTruckOnBridge -= 1


        if nowTruckOnBridge < bridge_length:
            # 다리에 트럭을 올릴 수 있는 조건 : 현재 다리가 버틸 수 있는 무게의 트럭이 있어야 하고, 다리가 포화상태가 아니어야 함.
            if truck_queue and nowWeight >= truck_queue[0]:
                bridge_queue.append([truck_queue.popleft(), time + bridge_length])
                # 다리가 버틸 수 있는 무게 갱신
                nowWeight -= bridge_queue[-1][0]
                nowTruckOnBridge += 1

    return time

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]

    print(solution(bridge_length, weight, truck_weights))