# 1958

'''
LCS : Longest Common Subsequence
공통 부분 문자열 중 가장 길이가 긴 문자열

Substring vs Subsequence

Substring : 전체 문자열에서 "연속된" 부분 문자열
Subsequence : 전체 문자열에서 "꼭 연속된 문자열인 것은 아닌" 부분 문자열

ex) ABCDEF / ACDGHI 의 공통 Subsequence : ACD

참고 : https://chanhuiseok.github.io/posts/algo-34/
'''

'''
내 예상 풀이 방법
1. DP를 활용한 알고리즘 이용해 첫번째 문자열과 두번째 문자열을 비교, LCS와 LCS의 길이를 return 받는다.
2. 위 과정에서 만든 함수를 재사용하여, return 값으로 받았던 LCS와 세번째 문자열을 비교하여 LCS와 LCS의 길이를 구한다.
3. LCS의 길이만 필요하므로, 길이만 따로 출력한다.
'''

# str_1 = input()
# str_2 = input()
# str_3 = input()

# m_LCS = ""
# result = 0
# def LCS(str1,str2):
#     m_LCS = ""
#     str1 = "0" + str1
#     str2 = "0" + str2
#     len_LCS = 0
#     arr_1 = list(str1)
#     arr_2 = list(str2)

#     # dp의 size : (str1 길이 + 1) X (str2 길이 + 1)
#     dp = [[0 for j in range(len(arr_1))] for i in range(len(arr_2))]
#     for row in range(1,len(arr_2)):
#         for col in range(1,len(arr_1)):
#             # print(row,col) # 행과 열이 잘 순환되는지 알아보기 위함
#             if arr_1[col] == arr_2[row]: # 같다면
#                 dp[row][col] = dp[row - 1][col - 1] + 1 # 대각선 왼쪽 윗 값 + 1
#             else: # 같지 않다면
#                 dp[row][col] = max(dp[row - 1][col],dp[row][col - 1]) 

#     len_LCS = dp[row][col] # LCS의 길이
#     
#     # 역추적하는 알고리즘으로 LCS 문자열 찾기
#     while(dp[row][col] != 0):
#         if dp[row][col] == dp[row - 1][col]:
#             row -= 1
#         elif dp[row][col]== dp[row][col - 1]:
#             col -= 1
#         else:
#             m_LCS = arr_1[col] + m_LCS
#             # print(row,col,m_LCS)
#             row -= 1
#             col -= 1
        
#     return m_LCS,len_LCS # dp의 마지막행 마지막열 값이 곧 LCS의 길이

# m_LCS,result = LCS(str_1,str_2) # 첫번째, 두번째 문자열과 비교하여 , 둘 사이의 LCS 추출
# m_LCS,result = LCS(m_LCS,str_3) # 추출한 LCS와 세번째 문자열과 비교하여 최종 LCS 추출
# # print(m_LCS)
# print(result) # LCS의 길이만 출력하면 끝

'''
LCS 알고리즘을 2번 돌리는 경우 예외사항이 생김

A: dababcf
B: ababdef
C: df

LCS(A,B): ababf
LCS(LCS(A,B),C): f
LCS(A,B,C): df

해가 유일하지 않다는것도 한몫함
LCS 2번 하는것과 3차원 DP의 차이점 : https://www.acmicpc.net/board/view/6859
'''

'''
3차원 DP는 시간복잡도가 O(n^3)이지만, 문자열의 각 최대 길이가 100이라 
    최악의 경우 10만번 비교하니 문제가 되지 않을 것이라 추측
2차원 DP에서 3차원 DP로 변경된 것일 뿐, 알고리즘은 바뀌지 않았으니 똑같은 방식으로 문제를 풀어볼 것. 대신 LCS의 길이만 추출하면 됨
'''

str_1 = input()
str_2 = input()
str_3 = input()

def LCS(str1,str2,str3):

    # 문자열 맨 앞에 0을 추가하여 문자 비교가 1번째 인덱스부터 이루어지도록 하기 위함
    str1 = "0" + str1
    str2 = "0" + str2
    str3 = "0" + str3

    # 리스트로 변환
    arr_1 = list(str1)
    arr_2 = list(str2)
    arr_3 = list(str3)

    # dp의 size : (str1 길이 + 1) X (str2 길이 + 1) x (str3 길이 + 1)
    # dp 내 모든 내용물은 0으로 초기화
    dp = ([[[0 for _ in range(len(arr_3))] for _ in range(len(arr_2))] for _ in range(len(arr_1))])
    
    # 3중 for문 : 시간복잡도 n^3
    for level in range(1,len(arr_3)):
        # 레벨(높이)
        for row in range(1,len(arr_2)):
            # 행
            for col in range(1,len(arr_1)):
                #열
                # print(col,row,level) # 열 -> 행 -> 레벨(높이) 잘 순환되는지 확인하기 위함

                if arr_1[col] == arr_2[row] == arr_3[level]: # 현재 비교중인 행/열/높이의 문자가 셋 다 같다면
                    dp[col][row][level] = dp[col - 1][row - 1][level - 1] + 1 # 대각선 이전 값 + 1
                else: # 같지 않다면
                    dp[col][row][level] = max(dp[col - 1][row][level], dp[col][row - 1][level], dp[col][row][level - 1]) 

    return dp[col][row][level] # LCS의 길이

print(LCS(str_1,str_2,str_3))