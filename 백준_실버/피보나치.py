# 9009
# fn-2 + fn-1 = fn : 피보나치

# 가장 적은 피보나치수의 합으로 입력값 표현하기


def toFibbo():
    fibbo = []
    result = []
    for i in range(0,n):
        now_num = numlist[i]
        num = 2
        fibbo.append(0)
        fibbo.append(1)

        # 입력된 정수보다 작은 모든 피보나치 배열 만들기
        while 1:
            if fibbo[-1] + fibbo[-2] > now_num:
                break
            fibbo.append(fibbo[num-1] + fibbo[num-2])
            num += 1
        
        find_index = len(fibbo) - 1
        while now_num >= 0 and find_index >= 0:
            if fibbo[find_index] <= now_num:
                result.append(fibbo[find_index])
                now_num -= fibbo[find_index]
            find_index -= 1
        result.remove(0) # 0은 필요없으니 삭제
        result.sort() # 오름차순 정렬
        
        # 출력 형식에 맞춰 출력하기
        for x in result:
            print(x,end=" ")
        print("")

        result.clear() # 비워서 초기화
        fibbo.clear() # 비워서 초기화
        


if __name__ == "__main__":
    n = int(input())
    numlist = []
    for _ in range(n):
        inum = int(input())
        numlist.append(inum)

    toFibbo()
    