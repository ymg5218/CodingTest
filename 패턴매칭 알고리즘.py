# POA #262

def match(P,S,n,m): 
    matched = False

    if(S[0] == P[0]):
        l = 0
        r = 0
        matched = True
        while(r < m and matched == True):
            matched = (matched == True) and (P[r] == S[l+r])
            r += 1
        if(matched == True):
            return 0
    
    l = 0
    while(l <= n - m and matched == False):
        l += 1
        r = 0
        matched = True

        while(r < m and matched == True):
            matched = (matched == True) and (P[r] == S[l + r])
            r += 1

    return l

pattern = "lol"
str = "algorithm"
result = match(pattern,str,len(str),len(pattern))


if(result < len(str) - len(pattern) + 1):
    print("[%s] 라는 패턴은 문자열에 존재하네요!"%(pattern))
    print("해당 패턴이 문자열 [%s]의 %d번째 인덱스부터 시작합니다."%(str,result))
else:
    print("패턴 [%s]이 문자열 [%s]에 존재하지 않습니다!"%(pattern, str))
