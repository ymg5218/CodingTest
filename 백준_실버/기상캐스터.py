# 10709
# 1초마다 1칸 움직이는 구름
# 각 구역마다 구름이 처음으로 등장한 시간 측정

def cloud_init(): # 각 구역의 첫 구름 시간 초기화
    for i in range(0,H):
        for j in range(0,W):
            if cloud[i][j] == "c":
                result_arr[i][j] = 0
    return result_arr
def cloud_flow():
    for time in range(1,W+1): # 구름은 1초에 한 칸, W초 동안 W칸 만큼 이동
        for i in range(0,H): # 구름 한 칸 이동
            del cloud[i][W-1]
            cloud[i].insert(0,".") # 구름 한 칸 이동 성공
            for j in range(0,W):
                if cloud[i][j] == "c" and result_arr[i][j] == -1: 
                    result_arr[i][j] = time # 구름 첫 등장 시간 책정

    for x in result_arr: # 이쁘게 출력
        for y in x:
            print(y,end=" ")
        print()

if __name__ == "__main__":
    H,W = map(int, input().split())
    cloud = [] # 구름의 현재 위치
    result_arr = [] # 최종 출력할 배열
    for i in range(0,H):
        result_arr.append([])
        cloud.append([])
        temp = input()
        for val in temp:
            cloud[i].append(val)
        for j in range(0,W):
            result_arr[i].append(-1)

    cloud_init() # 첫 구름 위치에 따른 각 지역 첫 구름 출몰 시간 초기화
    cloud_flow() # 시간 흐름에 따른 각 구역 첫 구름 출몰 시간 결과
    
    
    
    