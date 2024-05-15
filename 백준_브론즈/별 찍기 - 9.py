# 2446

N = int(input())

for i in range(N - 1, -1, -1):
    left_blank = " " * (N - 1 - i)
    left_start = "*" * i
    center_star = "*"
    right_star = "*" * i

    print(left_blank + left_start + center_star + right_star)

for i in range(1, N):
    left_blank = " " * (N - 1 - i)
    left_start = "*" * i
    center_star = "*"
    right_star = "*" * i

    print(left_blank + left_start + center_star + right_star)