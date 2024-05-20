# 13274

def solution():
    temp = []
    for _ in range(K):
        L, R, X = map(int, input().split())
        # X가 양수면 0 ~ L -2 까지는 무조건 작음
        if X > 0:
            if arr:
                l = L - 1
                r = R
                for i in range(L - 1):
                    temp.append(arr[i])
                
                is_l_break = False
                is_r_break = False

                while True:
                    if l == R:
                        is_l_break = True
                    
                    if r == N:
                        is_r_break = True

                    if is_l_break and is_r_break:
                        break
                    elif is_l_break:
                        temp.append(arr[r])
                        r += 1
                        continue

                    elif is_r_break:
                        temp.append(arr[l])
                        l += 1
                        continue


                    if arr[l] <= arr[r]:
                        temp.append(arr[l])
                        l += 1
                    else:
                        temp.append(arr[r])
                        r += 1
                
                arr.clear()

            else:
                for i in range(L - 1):
                    arr.append(temp[i])
                
                is_l_break = False
                is_r_break = False

                while True:
                    if l == R:
                        is_l_break = True
                    
                    if r == N:
                        is_r_break = True

                    
                    if is_l_break and is_r_break:
                        break

                    elif is_l_break:
                        arr.append(temp[r])
                        r += 1
                        continue
                    
                    elif is_r_break:
                        arr.append(temp[l])
                        l += 1
                        continue     

                    if temp[l] <= temp[r]:
                        arr.append(arr[l])
                        l += 1
                    else:
                        arr.append(arr[r])
                        r += 1

                temp.clear()

        # X가 음수면 R ~ N - 1까지는 무조건 큼
        else:
            l = 0
            r = L - 1

            is_l_break = False
            is_r_break = False

            if arr:
                while True:
                    if l == L - 1:
                        is_l_break = True
                    
                    if r == R:
                        is_r_break = True

                    if is_l_break and is_r_break:
                        break
                    
                    elif is_l_break:
                        temp.append(arr[r])
                        r += 1
                        continue

                    elif is_r_break:
                        temp.append(arr[l])
                        l += 1
                        continue

                    if arr[l] < arr[r]:
                        temp.append(arr[l])
                        l += 1
                    else:
                        temp.append(arr[r])
                        r += 1

                for i in range(R, N):
                    temp.append(arr[i])

                arr.clear()
            
            else:
                while True:
                    if l == L - 1:
                        is_l_break = True
                    
                    if r == R:
                        is_r_break = True

                    if is_l_break and is_r_break:
                        break
                    
                    elif is_l_break:
                        arr.append(temp[r])
                        r += 1
                        continue

                    elif is_r_break:
                        arr.append(temp[l])
                        l += 1
                        continue

                    if arr[l] < arr[r]:
                        arr.append(temp[l])
                        l += 1
                    else:
                        arr.append(temp[r])
                        r += 1
                
                for i in range(R, N):
                    arr.append(temp[i])

                temp.clear()

    return arr, temp
            
                    
                
                    

            
        


if __name__ == "__main__":
    N, K = map(int,input().split())
    arr = list(map(int, input().split()))

    arr, temp = solution()

    if arr:
        for i in range(N):
            print(arr[i], end=" ")
    else:
        for i in range(N):
            print(temp[i], end= " ")