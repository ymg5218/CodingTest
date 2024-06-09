# 11721

N = input()

start = 0
end = 10

while True:
    if start >= len(N):
        break
    if end >= len(N):
        print(N[start : ])
    else:
        print(N[start : end])

    start += 10
    end += 10