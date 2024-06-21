def back_tracking(now, used, used_cnt, length):
    global combi_nums
    global arr
    global largest
    # 조합 가능한 수 추가
    if now != "" and now not in combi_nums:
        # 2는 소수임
        if int(now) == 2:
            combi_nums.add(int(now))
            largest = max(largest, int(now))
        # 짝수이거나 1이면 애초에 넣지 않음
        elif int(now) % 2 != 0 and now != "1":
            combi_nums.add(int(now))
            largest = max(largest, int(now))
    if length == used_cnt:
        return
    
    for idx in range(length):
        if not used[idx]:
            used[idx] = True
            if now == "" and arr[idx] == "0":
                back_tracking("", used, used_cnt + 1, length)
            else:
                back_tracking(now + arr[idx], used, used_cnt + 1, length)
            used[idx] = False

def solution(numbers):
    global combi_nums
    global arr
    global largest

    arr = list(numbers)
    length = len(arr)

    # 조합 가능한 수 중 가장 큰 수를 담을 변수
    largest = 0

    # 조합 가능한 모든 수
    combi_nums = set()
    for i in range(length):
        used = [False] * length
        used[i] = True
        used_cnt = 1
        if arr[i] != "0":
            back_tracking(arr[i], used, used_cnt, length)
        # 수의 시작이 0인 경우
        else:
            back_tracking("", used, used_cnt, length)
    
    # answer 초기값 : 조합 가능 숫자의 개수
    answer = len(combi_nums)
    if answer == 0:
        return answer

    # 소수 판별 -> 에라토스테네스의 체
    # 시간복잡도 O(NlglgN) N 최대 9999999 ~> 4,000,000
    for n in range(2, int(largest**0.5) + 1):
        mul_op = 2
        now_num = n * mul_op
        while now_num <= largest:
            if answer == 0:
                return answer
            
            if now_num in combi_nums:
                combi_nums.remove(now_num)
                answer -= 1
            mul_op += 1
            now_num = n * mul_op

    return answer

if __name__ == "__main__":
    numbers = "9876543"
    print(solution(numbers))