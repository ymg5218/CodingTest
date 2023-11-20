# 5635

if __name__ == "__main__":
    n = int(input())

    people = []

    for _ in range(n):
        person = list(map(str, input().split()))
        people.append(person)
    
    result1 = sorted(people, key = lambda x : (int(x[3]), -int(x[2]), -int(x[1])))

    result2 = sorted(people, key = lambda x : (int(x[3]), int(x[2]), int(x[1])))
    print(result1[-1][0])
    print(result2[0][0])