# 17609

'''
0. 배열을 이용
1. 문자열의 맨 앞과 맨 뒤를 비교
1-1. 매칭 성공 시, 맨 앞 인덱스는 +1, 맨 뒤 인덱스는 -1 해서 또 비교..
1-2. 매칭 실패 시, 각각 한 칸 씩 건너 뛰어 비교를 진행
2. 건너 뛰었을 때, 매칭이 되면 계속 진행하고, 매칭이 되지 않으면 탐색 종료 
'''

# 위의 방법은 시간초과

'''
1. 문자열과 뒤집은 문자열을 비교
1-1. 같으면 return 0
1-2. 다르면 2단계로 넘어감
2. 앞/뒤를 각각 한 인덱스씩 없애 비교를 진행
2-1. 같으면 return 1
2-2. 다르면 return 2
'''

# import sys

# T = int(input())

# result = []

# for _ in range(T):
#     str = sys.stdin.readline().rstrip()

#     left = 0 
#     right = len(str) - 1
    
#     while(left < right):
#         # print(arr)
        
#         # 1. 뒤집었을 때 같은 경우
#         if str == str[::-1]:
#             result.append("0")
#             break
#         # 2. 뒤집었을 때 다른 경우
#         else:
#             # 만약 길이 1의 접두사/접미사가 같으면 각각 한 칸씩 중앙쪽으로 땡겨온다
#             if str[left] == str[right]:
#                 left += 1
#                 right -= 1
#             # 만약 다르면
#             # 2-1 왼쪽 인덱스 자리 문자를 삭제하고, 삭제한 후 문자를 뒤집었을 때와 비교하여 같은지 비교한다
#             # 2-2 오른쪽 인덱스 자리 문자를 삭제하고, 삭제한 후 문자를 뒤집었을 때와 비교하여 같은지 비교한다
#             else:
#                 temp_slice_left = str[:left - 1] + str[right:] # 2-1
#                 temp_slice_right = str[:left] + str[right + 1:] # 2-2
#                 if temp_slice_left == temp_slice_left[::-1]: # 문자 하나 지우니 회문 O
#                     result.append("1")
#                     break
#                 elif temp_slice_left != temp_slice_left[::-1]: # 문자 하나 지워도 회문 X
#                     result.append("2")
#                     break
#                 elif temp_slice_right == temp_slice_right[::-1]: # 문자 하나 지우니 회문 O
#                     result.append("1")
#                     break
#                 elif temp_slice_right != temp_slice_right[::-1]: # 문자 하나 지워도 회문 X
#                     result.append("2")
#                     break

# for i in range(len(result)):
#     print(result[i])

# 이 방법도 시간초과. slice를 사용하지 않고 해보자

'''
0. 문자열 접두사 == 접미사 비교 함수 선언
1. 문자열을 받아와, 0번에서 선언한 함수에서 맨 앞 == 맨 뒤 비교 후, 중앙으로 당겨온다. 만약 끝까지 같다면 return 0
2. 중간에 다르다면, 원코 함수에서 재수행하도록 동작
2-1. 앞 + 1인 case와 맨 뒤 + 1인 case 각각을 따로따로 구분하여, 1번 방식과 동일하게 비교한다
3. 각 case 중, 하나라도 더 미스매치가 일어나면 return False, 끝까지 매칭된다면 return True
--> 굳이 각 케이스를 모두 끝까지 비교하는 이유 : abbab같은 입력예시 때문
--> 맨 왼쪽을 자르면 bbab로 회문이 아니지만, 맨 오른쪽을 자르면 abba로 회문임
4. 다시 처음 비교 함수로 돌아와, 하나라도 True인 case가 존재하면(or 연산자 이용) return 1, 둘다 False라면 return 2
'''

T = int(input())
result = [] # 정답 출력용

def palindrome(left,right,str):
    while(left < right): # 왼쪽 참조 인덱스가 오른쪽 참조 인덱스보다 같거나 크면 종료
        if str[left] == str[right]: # 일치 O
            left += 1
            right -= 1
        else: # 일치 X
            left_jump_case = onecoin(left + 1,right,str) # 왼쪽에서 한 칸 뛴 케이스
            right_jump_case = onecoin(left,right - 1,str) # 오른쪽에서 한 칸 뛴 케이스
            if (left_jump_case or right_jump_case): # 둘 중 하나라도 유사회문인 케이스(True)가 존재한다면
                return 1
            else: # 하나도 회문인 케이스가 없다면
                return 2
    return 0 # 첫 번째 시도에 끝까지 매칭이 성공했다면 : 회문

def onecoin(left,right,str):
    while(left < right): # 왼쪽 참조 인덱스가 오른쪽 참조 인덱스보다 같거나 크면 종료
        if str[left] == str[right]:
            left += 1
            right -= 1
        else: # 원코 줬는데, 또 틀리면 가차없이 False
            return False
    return True # 끝까지 매칭되면 True


for _ in range(T):
    str = input()
    result.append(palindrome(0,len(str) - 1,str))

for i in range(T):
    print(result[i])
