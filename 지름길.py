# 1446

# 모든 지름길은 일방통행 : 단방향 간선

# 길이 D의 고속도로에 N개의 지름길 존재

# 반복문을 통해 진행하니 복잡도가 너무 높았음 = > 해결책 : 힙을 활용한 구현
# 참고 - heapq : https://littlefoxdiary.tistory.com/3
# 참고 - 힙 구조를 이용한 다익스트라 : https://velog.io/@tks7205/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python


import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start)) # 힙 빌드업
    distance[start] = 0

    while heap: # 
        print(heap)
        dis, now = heapq.heappop(heap) # 우선순위가 가장 낮은 값 = 가장 작은 거리가 나온다.

        if distance[now] < dis :
            continue # 이미 최솟값이 distance 배열의 now번째 인덱스에 저장돼있다면 무시

        for element in road[now]:
            length = dis + element[1] # 배열의 각 요소 1번째 인덱스는 거리. 현재 dis와 더하여 length에 저장

            if distance[element[0]] > length: # 만약 length가 이미 저장된 총 거리보다 작다면
                distance[element[0]] = length # 최솟값으로 치환
                heapq.heappush(heap,(length,element[0]))
    




if __name__ == "__main__":
    INF = 1e8
    N,D = map(int,input().split()) # 지름길 개수, 고속도로 길이 입력
    road = [[]for _ in range(0,D+1)] # 거리 1 마다 노드가 있다고 판단함
    distance = [INF] * (D+1) # 거리

    for i in range(0,D): # 모든 노드는 거리 1로 초기화
        road[i].append((i+1,1))
    
    for i in range(0,N):
        start, end, cost = map(int,input().split())
        if end <= D: # 지름길의 끝점이 고속도로 최종 목적지를 넘어가면 무효
            road[start].append((end,cost))
        

    dijkstra(0)
    print(distance[D])
    
        