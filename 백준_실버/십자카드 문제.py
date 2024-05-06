# 2659

def find_clocknum(num):
    str_num = str(num)
    min_clocknum = 10000
    for i in range(4):
        now_clocknum = ""
        for j in range(4):
            now_clocknum += str_num[(i + j) % 4]
        min_clocknum = min(min_clocknum, int(now_clocknum))
    
    return min_clocknum


def solution():
    card_num = int(card[0] + card[1] + card[2] + card[3])
    card_clocknum = find_clocknum(card_num)

    # 1111 ~ 9999 까지 0이 없는 수 조합 만들기
    for thousand in range(1, 10):
        for hundred in range(1, 10):
            for ten in range(1, 10):
                for one in range(1, 10):
                    num = thousand * 1000 + hundred * 100 + ten * 10 + one
                    clocknum = find_clocknum(num)
                    arr.add(clocknum)
                    if clocknum == card_clocknum:
                        result = sorted(arr)
                        return result.index(card_clocknum)



if __name__ == "__main__":
    card = list(map(str, input().split()))
    arr = set()

    print(solution() + 1)