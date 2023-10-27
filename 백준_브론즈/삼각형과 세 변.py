# 5073

while True:
    arr = list(map(int,input().split()))
    if arr[0] == arr[1] == arr[2] == 0:
        break
    if arr[0] == arr[1] == arr[2]:
        print("Equilateral")
    else:
        if arr[0] + arr[1] <= arr[2] or arr[0] + arr[2] <= arr[1] or arr[1] + arr[2] <= arr[0]:
            print("Invalid")
        else:
            if arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
                print("Isosceles")
            else:
                print("Scalene")
        