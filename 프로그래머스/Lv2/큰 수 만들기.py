def solution(number, k):
    num_list = list(number)

    while k > 0:
        remove_set = {}
        for i in range(1, len(num_list) - 1):
            if num_list[i - 1] < num_list[i]:
                remove_set[i - 1] = True
                k -= 1

       
    
    answer = "".join(num_list)

    return answer

if __name__ == "__main__":
    number = "4177252841"
    k = 4

    print(solution(number, k))