
def solution(arr):
    sum = 0
    for n in arr:
        if n % 2 == 1:
            sum += n
    return sum

if __name__ == "__main__":
    T = int(input())
    
    for i in range(T):
        arr = list(map(int, input().split()))
        print(f'#{i + 1} {solution(arr)}')