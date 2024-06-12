def solution(people,limit):
    answer = 0

    people.sort()
    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1

    return answer

if __name__ == "__main__":
    people = [40, 40, 20, 80, 40, 70, 90]

    limit = 100

    print(solution(people, limit))