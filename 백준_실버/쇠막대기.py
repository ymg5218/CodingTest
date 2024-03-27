# 10799

'''
1. 괄호 기호 문자열 bracket 입력받음

2. 스택 자료구조 stack 선언, 총 파이프 개수를 담을 cnt 선언

3. bracket을 처음부터 끝까지 순회
    3-1. '(' 기호 시, 파이프의 시작 or 레이저포인트 지점을 알림. 일단 stack에 append 
    3-2. ')' 기호 시, 두 가지 경우가 존재함
        3-2-1. 바로 이전 기호가 '(' -> 레이저 포인트이므로 stack의 top을 pop. 나머지 stack의 '(' 요소 개수만큼 현재 파이프가 쌓여있다는 의미이므로 절단된 부분까지의 개수를 cnt에 더해줌.
        3-2-2. 바로 이전 기호가 ')' -> 파이프의 끝이라는 의미이므로, stack의 top을 pop하고 해당 파이프의 존재가 유효해졌으므로 cnt에 1을 더해줌

4. cnt 출력
'''

def solution():
    cnt = 0

    stack = []

    # 시간복잡도 O(n)
    # bracket 순회
    for i in range(len(bracket)):
        # '(' 기호 시, 파이프의 시작 or 레이저포인트 지점을 알림. 일단 stack에 append 
        if bracket[i] == '(':
            stack.append(bracket[i])
        # ')' 기호 시, 두 가지 경우가 존재함
        else:
            # 바로 이전 기호가 '('
            if bracket[i - 1] == '(':
                stack.pop()
                cnt += len(stack)
            # 바로 이전 기호가 ')'
            else:
                stack.pop()
                cnt += 1
    return cnt

if __name__ == "__main__":
    bracket = input()

    print(solution())
