# 11005

N,B = map(int,input().split())

dict = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,
        "Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}

digit = 0
mod = 0
result = ""

while(N > 0):
    mod = N % B
    if mod >= 10:
        for key, value in dict.items():
            if value == mod:
                result += key
    else:
        result += str(mod)
    N //= B

for i in range(len(result)-1,-1,-1):
    print("%s" %result[i], end="")