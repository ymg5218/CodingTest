def solution(numbers, hand):
    answer = ""
    pad = {
        1 : (0, 0),
        2 : (0, 1),
        3 : (0, 2),
        4 : (1, 0),
        5 : (1, 1),
        6 : (1, 2),
        7 : (2, 0),
        8 : (2, 1),
        9 : (2, 2),
        0 : (3, 1)
    }
    left = (3, 0)
    right = (3, 2)

    now_idx = 0
    while now_idx < len(numbers):
        now = pad[numbers[now_idx]]

        # 왼손 사용 영역
        if now[1] == 0:
            answer += "L"
            left = now
        # 오른손 사용 영역
        elif now[1] == 2:
            answer += "R"
            right = now
        
        # 중간열
        else:
            left_movement = abs(left[0] - now[0]) + abs(left[1] - now[1])
            right_movement = abs(right[0] - now[0]) + abs(right[1] - now[1])

            if left_movement < right_movement:
                answer += "L"
                left = now
            elif left_movement > right_movement:
                answer += "R"
                right = now
            else:
                if hand == "right":
                    answer += "R"
                    right = now
                else:
                    answer += 'L'
                    left = now

        now_idx += 1
        

    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    print(solution(numbers, "right"))