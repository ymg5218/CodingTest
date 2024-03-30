import itertools

def solution(dice):
    answer = []

    length = len(dice)

    # 각 주사위에 인덱스 번호 부여
    dice_idx = [i for i in range(length)]

    A_get = length // 2
    
    # A가 A_get 만큼 주사위를 고를 수 있는 모든 조합
    A_cases = list(itertools.combinations(dice_idx, A_get))

    for A_case in A_cases:
        B_case = dice_idx[:]
        for i in range(A_get):
            B_case.remove(A_case[i])
        
        pointer = {}
        for i in range(length):
            pointer[i] = 0
        
        point = 0

        while pointer[length - 1] <= 5 and point <= 5:
            if pointer[point] == 5:
                pointer[point] = 0
                point += 1
                continue
            
            A_sum = 0
            for d_idx in A_case:
                A_sum += dice[d_idx][pointer[d_idx]]
            if pointer[point] != 5:
                pointer[point] += 1
            print(A_sum)
        
            
        # print(B_case)
    

    return answer

if __name__ == "__main__":
    dice = [[1,2,3,4,5,6], [3,3,3,3,4,4], [1,3,3,4,4,4], [1,1,4,4,5,5]]
    solution(dice)