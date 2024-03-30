def solution(friends, gifts):
    length = len(friends)
    '''
    무지 : 0
    라이언 : 1
    프로도 : 2
    네오 : 3
    '''

    # 각 친구들의 인덱스번호를 저장할 딕셔너리
    index_dict = {}
    idx = 0
    for friend in friends:
        index_dict[friend] = idx
        idx += 1
    
    # 선물 주고받은 개수 레코드 테이블
    '''
    * row = col인 요소는 자기 자신이므로 연산에서 제외시켜야함
    '''
    gift_record = [[0 for _ in range(length)] for _ in range(length)]
    
    # gift_record 채우기
    for gift in gifts:
        giver, taker = map(str, gift.split())
        gift_record[index_dict[giver]][index_dict[taker]] += 1
    
    
    # 선물지수 레코드 테이블
    '''
    0열 : 준 선물
    1열 : 받은 선물
    2열 : 선물 지수
    '''
    gift_score = [0 for _ in range(length)]

    # 선물지수 레코드 테이블 데이터 삽입
    for row in range(length):
        for col in range(length):
            if row == col:
                continue
            gift_score[row] += gift_record[row][col]
            gift_score[col] -= gift_record[row][col]
    
    result = [0 for _ in range(length)]
    # 결과 출력 로직
    for row in range(length):
        for col in range(row + 1, length):
            if gift_record[row][col] > gift_record[col][row]:
                result[row] += 1
            elif gift_record[row][col] < gift_record[col][row]:
                result[col] += 1
            else:
                if gift_score[row] > gift_score[col]:
                    result[row] += 1
                elif gift_score[col] > gift_score[row]:
                    result[col] += 1
    
    return max(result)

if __name__ == "__main__":
    friends = ['muzi', 'ryan' ,'frodo', 'neo']
    gifts = ['muzi frodo', 
             'muzi frodo',
             'ryan muzi',
             'ryan muzi',
             'ryan muzi',
             'frodo muzi', 
             'frodo ryan',
             'neo muzi'
             ]
    solution(friends, gifts)