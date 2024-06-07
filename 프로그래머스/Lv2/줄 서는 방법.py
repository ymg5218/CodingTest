'''
n <= 20 자연수
20! = 2,432,902,008,176,640,000 ~= 10**19
=> 브루트포스로 구하면 시간초과

문제 접근
1. 정렬 순서
2. 큰 문제를 부분 문제로 쪼갤 수 있음
'''

def solution(n, k):
    answer = []
    
    block_size = 1

    for i in range(1, n + 1):
        block_size *= i

    # 인덱스 번호 = 자리수 동일시키기 위해 0번째 인덱스는 더미 값
    num_list = [i for i in range(n+1)]
    
    for seq in range(n):
        # 현재 자리수 기준 정렬 시, 블럭 당 사이즈 구하기
        block_size //= (n - seq)

        now_block_start = 1
        now_block_end = block_size

        for i in range(1, n + 1):
            # 현재 블럭 안에 찾는 부분 집합이 존재하면 수행
            if now_block_start <= k <= now_block_end:
                # 현재 블럭의 부분 집합에서 몇 번째 순번을 찾아야 하는지 k 값 수정
                k = k - now_block_start + 1

                # 현재 블럭의 가장 큰 자리수를 answer에 append
                answer.append(num_list[i])

                # 해당 자리수에 사용된 수는 remove
                num_list.remove(num_list[i])
                break

            # 아니라면 다음 블럭 범주를 탐색
            now_block_start += block_size
            now_block_end += block_size

    return answer

if __name__ == "__main__":
    n = 3
    k = 5
    print(solution(n, k))
