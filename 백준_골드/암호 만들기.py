# 1759

'''
내 예상 풀이
1. 입력받은 알파벳을 사전순으로 정렬한다.(오름차순)
2. 백트래킹을 이용해 모든 경우의 수를 판단한다.(최악의 경우 15 combination 7 == 6435)
3. 조합해 본 조합에서, 자음 최소 2개 이상, 모음 최소 1개 이상 조건을 충족하는지 확인.
4. 조건에 충족한다면 print
'''

'''
함수명 : check
매개변수 : result -> 조건을 충족하는지 체크할 암호 조합
역할 : result가 조건을 충족하면 True, 충족하지 않으면 False return
'''

def check(result):
    co_cnt, vo_cnt = 0, 0 # 자음,모음 개수 체크
    for i in range(L):
        # 모음인가?
        if result[i] in ["a","e","i","o","u"]:
            vo_cnt += 1
        # 자음인가?
        else:
            co_cnt += 1
    # 조건(모음이 최소 1개, 자음이 최소 2개)을 충족하지 않는가?
    if co_cnt < 2 or vo_cnt < 1:
        return False
    else:
        # 조건을 충족하는가?
        return True

'''
함수명 : solution
매개변수 : append_idx -> result에 추가할 arr 요소의 인덱스 번호
역할 : 백트래킹을 이용하여 모든 경우의 수를 체크한다.
'''
def solution(append_idx):
    global arr
    global L,C
    global result
    
    if len(result) == L:
        if check(result) == True:
            for idx in range(L):
                print(result[idx], end="")
            print()
        return  

    # arr의 append_idx 요소부터 result에 하나씩 append.
    # 모든 암호 조합을 따져보려고 함.
    for idx in range(append_idx, C):
        result.append(arr[idx]) 
        solution(idx + 1) # idx + 1 번째 요소를 append하기 위해 매개변수 idx + 1로 재귀 수행
        result.pop() # 다른 경우의 수도 따져보기 위해, 가장 마지막에 추가한 요소 pop


if __name__ == "__main__":
    L,C = map(int,input().split())
    arr = sorted(list(map(str,input().split())))
    result = []
    solution(0)