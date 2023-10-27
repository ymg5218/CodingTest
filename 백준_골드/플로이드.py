# 11404


def Floyd_Warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                city[i][j] = min(city[i][j], city[i][k] + city[k][j])
    
    for row in range(1, n+1):
        for col in range(1, n+1):
            if city[row][col] == INF:
                print(0,end = ' ')
            else:
                print(city[row][col],end = ' ')
        print()

if __name__ == "__main__":

    INF = 100000 * 100 + 1

    n = int(input())
    
    # 각 도시까지의 최단경로 데이터를 저장할 n+1 * n+1 사이즈의 2차원배열 생성
    # 0행 0열은 더미 값.
    # 특정 두 도시끼리 버스 경로에 대해 플로이드-워셜 알고리즘을 이용해 최소값을 게속 갱신해야 하므로 각 요소는 최대값으로 초기화
    city = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    # city의 대각선 요소는 같은 도시끼리의 경로에 대한 최소시간이므로 0으로 초기화
    for dia in range(n+1):
        city[dia][dia] = 0
    
    m = int(input())

    for _ in range(m):
        a, b, time = map(int,input().split())
        # a 도시에서 b 도시로 가는 버스가 존재하며, 시간은 time만큼 걸림.
        # city[a][b]는 a에서 b로 가는 최소시간을 저장할 것이며, 초기 소요 시간인 time을 저장한다.
        # a 도시에서 b로 가는 버스의 소요 시간이 2개 이상일 경우, 최소값만을 유효하게하기 위해 min 함수 사용.
        city[a][b] = min(time, city[a][b])
    
    
    Floyd_Warshall()
    
    
    
        
