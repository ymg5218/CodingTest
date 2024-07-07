def solution(answers):
    answer = []

    first_idx = 0
    first_cnt = 0
    first = [1, 2, 3, 4 ,5]
    first_len = 5

    second_idx =  0
    second_cnt = 0
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    second_len = 8

    third_idx = 0
    third_cnt = 0
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    third_len = 10

    answers_idx = 0

    while (answers_idx < len(answers)):
        if answers[answers_idx] == first[first_idx]:
            first_cnt += 1

        if answers[answers_idx] == second[second_idx]:
            second_cnt += 1

        if answers[answers_idx] == third[third_idx]:
            third_cnt += 1

        answers_idx += 1
        first_idx = (first_idx + 1) % first_len
        second_idx = (second_idx + 1) % second_len
        third_idx = (third_idx + 1) % third_len

    max_cnt = max(first_cnt, second_cnt, third_cnt)

    if first_cnt == max_cnt:
        answer.append(1)

    if second_cnt == max_cnt:
        answer.append(2)

    if third_cnt == max_cnt:
        answer.append(3)

    return answer

if __name__ == "__main__":
    answers = [1,2,3,4,5]

    print(solution(answers))