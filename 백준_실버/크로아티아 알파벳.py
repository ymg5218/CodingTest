# 2941

'''
1. 입력 받음
2. 크로아티아 알파벳의 '부분 알파벳'을 _pattern에 따로 담음
2-1. 크로아티아 알파벳 pattern에 담음
3. 반복문 수행. idx가 입력받은 문자열의 길이보다 크거나 같으면 종료
    1. temp에 s[idx] 담아놓고, 해당 문자가 _pattern에 존재하는지 검사
    1-1. 존재함 : temp에 s[idx+1]을 추가로 담음
    1-1-1. temp가 존재함. 만약 dz라면 추가로 s[idx+2] 또한 더해서, dz= 인지 검사
    1-1-2. temp가 존재하지 않음 : s[idx]은 일반 알파벳으로 취급. idx와 cnt를 1 증가시키고 다시 반복문 수행
    1-2 존재하지 않음: 해당 문자는 일반 알파벳과 같으니, idx, cnt를 1 증가시키고 다시 반복문 수행
4. 최종 cnt 출력
'''

_pattern = ["c","=","d","-","z","l","j","n","s"]
pattern = ["c=","c-","dz=","d-","lj","nj","s=","z="]
s = input()

idx = 0
cnt = 0

while(idx < len(s)):
    temp = s[idx]
    if temp in _pattern and idx + 1 < len(s):
        temp += s[idx + 1]
        if temp == "dz" and idx + 2 < len(s):
            temp += s[idx + 2]
            if temp == "dz=":
                cnt += 1
                idx += 3
                continue
        else:
            if temp in pattern:
                cnt += 1
                idx += 2
                continue
    
    cnt += 1
    idx += 1


print(cnt)