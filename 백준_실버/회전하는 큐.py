# 1021

from collections import deque
import copy

# 순방향
def forward(queue, search_num):
    _cnt = 0
    _queue = copy.deepcopy(queue)
    while _queue[0] != search_num:
        temp = _queue.popleft()
        _queue.append(temp)
        _cnt += 1
    return _cnt, _queue

# 역방향
def reverse(queue, search_num):
    _cnt = 0
    _queue = copy.deepcopy(queue)
    while _queue[0] != search_num:
        temp = _queue.pop()
        _queue.appendleft(temp)
        _cnt += 1
    return _cnt, _queue

def solution(queue):
    cnt = 0
    for idx in range(M):
        search_num = find_num[idx]
        # 원하는 값이 리스트의 첫 번째에 오도록 하기 위해 필요한 최소 연산 개수 뽑아내기
        for_result_cnt, for_result_queue = forward(queue, search_num)
        rev_result_cnt, rev_result_queue = reverse(queue, search_num)
        
        if for_result_cnt <= rev_result_cnt:
            queue = for_result_queue
            cnt += for_result_cnt
        else:
            queue = rev_result_queue
            cnt += rev_result_cnt
            
        queue.popleft()

    print(cnt)

if __name__ == "__main__":
    N, M = map(int, input().split())
    find_num = list(map(int, input().split()))

    queue = deque([i+1 for i in range(N)])
    solution(queue)