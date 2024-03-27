# 10799

def solution():
    # 스택
    stack = []
    
    # 마지막으로 탐색한 기호 저장 변수
    last = bracket[0]

    # 탐색 순번 변수
    search_num = 1

    # 레이저 포인트
    cut_point = []

    # 파이프
    pipe = []

    for i in range(1, len(bracket)):
        '''
        현재 탐색 기호가 마지막 탐색 기호와 같다
        == 파이프 길이 연장 중
        '''
        if bracket[i] == last:
            


if __name__ == "__main__":
    # 입력값
    bracket = input()

    solution()
    
