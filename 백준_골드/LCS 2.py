# 9251

# LCS 3 문제랑 비슷해서 조금 수정하고 제출함

str_1 = input()
str_2 = input()

def LCS(str1,str2):
    m_LCS = ""
    str1 = "0" + str1
    str2 = "0" + str2
    len_LCS = 0
    arr_1 = list(str1)
    arr_2 = list(str2)

    # dp의 size : (str1 길이 + 1) X (str2 길이 + 1)
    dp = [[0 for j in range(len(arr_1))] for i in range(len(arr_2))]
    for row in range(1,len(arr_2)):
        for col in range(1,len(arr_1)):
            # print(row,col) # 행과 열이 잘 순환되는지 알아보기 위함
            if arr_1[col] == arr_2[row]: # 같다면
                dp[row][col] = dp[row - 1][col - 1] + 1 # 대각선 왼쪽 윗 값 + 1
            else: # 같지 않다면
                dp[row][col] = max(dp[row - 1][col],dp[row][col - 1]) 

    len_LCS = dp[row][col] # LCS의 길이
    
    # 역추적하는 알고리즘으로 LCS 문자열 찾기
    while(dp[row][col] != 0):
        if dp[row][col] == dp[row - 1][col]:
            row -= 1
        elif dp[row][col]== dp[row][col - 1]:
            col -= 1
        else:
            m_LCS = arr_1[col] + m_LCS
            # print(row,col,m_LCS)
            row -= 1
            col -= 1
        
    return len_LCS,m_LCS # dp의 마지막행 마지막열 값이 곧 LCS의 길이
result1, result2 = LCS(str_1,str_2)
print(result1,result2)