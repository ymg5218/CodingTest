# 카카오코딩 1
# 아이디 길이는 3자 이상, 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 마침표(.) 문자만 사용할 수 있음.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며, 연속으로 사용할 수 없습니다.
# 규칙에 맞는지 검사하고, 맞지 않는 경우 새로운 아이디를 추천해줌.

#
import re


def createID():  # 아이디 생성
    new_id = input("신규 ID를 입력하세요 : ")
    new_id = new_id.lower()  # 소문자로 변환
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)
    return new_id


def checkDot(new_id):  # 연속된 마침표 제거 함수
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    return new_id  # 연속된 온점 중복삭제 후의 id를 반환


def recheckDot(new_id):  # 온점이 처음이나 마지막에 위치하면 제거
    if(new_id[0] == '.'):  # 처음이 온점이면 삭제
        if(len(new_id) > 1):
            new_id = new_id[1:]
        else:
            new_id = " "

    if(new_id[-1] == "."):
        if (len(new_id) > 1):
            new_id = new_id[:-1]
        else:
            new_id = " "
    return new_id  # 수정된 아이디 반환



def checkLong(new_id):  # 문자열이 16자 이상이면 실행
    new_id = new_id[:15]  # 15까지 자름
    new_id = recheckDot(new_id)
    return new_id


def checkShort(new_id):  # 문자열이 2자 이하이면 실행
    new_id = plusA(new_id)  # 문자열이 공백이면 실행
    while(len(new_id) < 3):  # 길이가 3이 될때까지 마지막 문자 반복삽입
        new_id = new_id + new_id[-1]
    return new_id


def plusA(new_id):
    new_id = new_id.replace(" ", "a")
    return new_id


id = createID()  # 아이디 생성 함수 실행

id = checkDot(id)  # 연속된 온점 검사 함수 실행 - 매개변수 : 규칙 의거 수정 아이디

id = recheckDot(id)  # 처음과 마지막 온점 검사 함수 실행 - 매개변수 : 연속된 중복온점 수정 아이디

if(len(id) > 15):  # 최종 수정 아이디의 길이가 16이상일 때 실행
    id = checkLong(id)  # 규격 외 길이 제거 함수 실행 - 매개변수 : 최종 규칙수정 아이디
    print(id)  # 최종 추천 아이디 출력

elif(len(id) < 3):  # 최종 수정 아이디의 길이가 2 이하일 때 실행
    id = checkShort(id)  # 규격 외 길이 추가 함수 실행 - 매개변수 : 최종 규칙수정 아이디
    print(id)  # 최종 추천 아이디 출력

else:
    print(id)  # 길이가 규격 내라면 최종 규칙수정 아이디 출력