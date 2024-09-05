def solution(k, tangerine):
    answer = 0

    dict = {}
    for idx in range(len(tangerine)):
        if tangerine[idx] in dict:
            dict[tangerine[idx]] += 1
        else:
            dict[tangerine[idx]] = 1

    sorted_by_cnt = []

    for _, value in dict.items():
        sorted_by_cnt.append(value)

    # 내림차순 정렬
    sorted_by_cnt.sort(reverse=True)

    for cnt in sorted_by_cnt:
        k -= cnt
        answer += 1
        if k <= 0:
            break

    return answer

if __name__ == "__main__":
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))