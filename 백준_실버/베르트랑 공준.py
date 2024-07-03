# 4948

def findPrime():
    # 최대 123456 * 2 + 1
    num_list = [True for _ in range(123456 * 2 + 1)] # +1을 또 한 이유는 0번째 인덱스는 더미인덱스로 두기 위함
    num_list[0] = False
    for num in range(2, 123456 * 2 + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                num_list[num] = 0

    return num_list
            

if __name__ == "__main__":
    prime = findPrime()

    while True:
        n = int(input())
        if n == 0:
            break
        
        cnt = 0
        for i in range(n + 1, 2 * n + 1):
            if prime[i] == 1:
                cnt += 1

        print(cnt)
    