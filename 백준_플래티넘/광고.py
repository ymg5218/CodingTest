# 1305

if __name__ == "__main__":
    L = int(input())
    s = input()
    
    table = [0 for _ in range(L)]
    i = 0
    for j in range(1, L):
        while i > 0 and s[i] != s[j]:
            i = table[i - 1]
        
        if s[i] == s[j]:
            i += 1
            table[j] = i
            
    print(L - table[-1])