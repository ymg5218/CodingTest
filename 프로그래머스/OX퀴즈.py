# 프로그래머스 _ OX퀴즈
answer = []

def solution(quiz):
    idx = 0
    while(idx < len(quiz)):
        print(quiz[idx])
        new_quiz = quiz[idx].replace(" ","") # 공백 제거
        op,result = new_quiz.split("=") # = 연산자 기준 나눔
        if eval(op) == int(result):
            answer.append("O")
        else:
            answer.append("X")
        idx += 1
    return answer
# quiz = ["3 - 4 = -3", "5 + 6 = 11"]
# print(solution(quiz))