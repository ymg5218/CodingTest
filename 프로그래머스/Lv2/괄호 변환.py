# u가 올바르지 못한 괄호 문자열이면 양 옆 괄호를 삭제 후, 나머지 괄호들을 뒤집어야 함.
def u_isNotValid(_u):
    u = ""
    for i in range(1, len(_u) - 1):
        if _u[i] == "(":
            u += ")"
        else:
            u += "("

    return u


# 올바른 괄호 문자열인지 확인
def isValid(bracket):
    stack = []
    now_idx = 0
    while now_idx < len(bracket):
        now = bracket[now_idx]
        if now == "(":
            stack.append(now)
        else:
            # 스택에 아무것도 없는데 ) 로 시작하면 절대 올바를 수 없는 괄호
            if not stack:
                # 올바르지 않은 괄호 문자열
                return False
            # 스택에 뭔가 있다면 무조건 ( 일 것 -> stack.pop()
            else:
                stack.pop()
        now_idx += 1

    return True


def solution(p):
    answer = ""

    now_idx = 0
    length = len(p)

    bracket = []
    left = 0
    right = 0
    while now_idx < length:
        bracket.append(p[now_idx])
        if p[now_idx] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            v = p[now_idx + 1:]
            if isValid(bracket):
                u = "".join(bracket)
                answer += u
                # u를 제외한 나머지 문자 v에 대해 재귀적으로 접근
                answer += solution(v)
            else:
                u = u_isNotValid(bracket)
                # 순서 1. (  + v에 대해 1단계부터 재귀적으로 수행한 결과 + ) 를 이어 붙임
                temp = "(" + solution(v) + ")"
                answer += temp
                # 순서 2. u를 이어 붙임
                answer += u
            break

        now_idx += 1

    return answer


if __name__ == "__main__":
    p = "()))((()"

    print(solution(p))