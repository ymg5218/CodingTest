# 1599

# 민식어 선언 : 딕셔너리 이용 // "ng" : "L" 은 따로 번역하기 위해 딕셔너리에 추가하지 않았음
msl = {"a":"A","b":"B","k":"C","d":"D","e":"E","g":"F","h":"G","i":"H","l":"I","m":"J","n":" K"
       ,"o":"M","p":"N","r":"O","s":"P","t":"Q","u":"R","w":"S","y":"T"} 
trans_dic = {} # 번역한 문자(key) : 민식어 문자(value)로 저장하기 위함.
               # key값으로 저장해도 되는 근거는, 문제에 '모든 단어는 중복되지 않는다'라고 선언했기 때문.
N = int(input())

for _ in range(N):
    str = input()
    is_pass = False # ng 발견 시 True로 전환, 이후 번역목적 반복문에서 True가 감지되면 False로 바꾸고 번역 건너 뛸 것. 
                    #                                            ==> ng 두 글자를 한 글자로 번역했으니 건너뛰기 위함
    temp = list(str) # 문자를 글자 단위로 쪼개기
    temp_str = "" # 민식어 -> 영어 번역한 문자열 임시 저장

    # 민식어 -> 영어 번역 : 반복문 start
    for i in range(len(temp)):
        if is_pass == True: # 건너뛰어야 하면
            is_pass = False # False로 바꾸고 건너뛴다.
            continue
        elif i != len(temp) - 1 and temp[i] == 'n' and temp[i+1] == 'g': # 맨 마지막 인덱스를 참조중이지 않으면서, n 다음 인덱스가 g라면 ng이므로 묶어서 L로 번역한다.
            temp_str += 'L'
            is_pass = True # 두 글자를 한 글자로 번역했으니, is_pass를 True로 전환하고 턴 종료
        else:
            temp_str += msl[temp[i]]
    trans_dic[temp_str] = str # temp_str 즉, 영어로 번역한 문자열들을 key값으로, str 즉, 입력받은 민식어 기반 문자열을 value값으로 저장.

for value in dict(sorted(trans_dic.items())).values(): # 딕셔너리를 key 값 중심으로 정렬하여 사전순으로 배치한 다음, value값을 하나하나 출력하면 끝
    print(value)

