def solution(clothes):
    answer = 1

    dict = {}
    categories = []

    for c, category in clothes:
        if category not in dict:
            dict[category] = ["", c]
            categories.append(category)
        else:
            dict[category].append(c)

    for _, value in dict.items():
        answer *= len(value)

    # 아무것도 안 입는 조합은 빼야함
    return answer - 1

if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))