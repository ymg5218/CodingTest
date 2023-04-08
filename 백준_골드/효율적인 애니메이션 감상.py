# 27313

'''
예상 풀이 방법
1. N_arr을 오름차순 정렬한다
<종료조건>에 부합하기 전까지 계속 반복
2. N_arr의 최대값이 M보다 크다면 최대값들을 삭제한다
3. N_arr의 최대값이 M보다 작다면 N_arr[-K:]를 묶어서 애니를 감상
    감상한 애니는 delete
3-1. M - (감상한 애니들 중 가장 긴 소요시간)
3-2. 애니 감상 개수를 카운팅
4. 카운팅한 애니 감상 개수를 print
'''
# import sys
# input = sys.stdin.readline

# N,M,K = map(int,input().split())

# N_arr = list(map(int,input().split()))

# cnt = 0

# N_arr.sort()

# if N_arr[0] > M: # 어느 영화도 못보는 경우면 0 출력 후 종료
#     print(cnt)
#     exit()

# '''
# 종료 조건
# 1. 애니를 볼 수 있는 시간 M을 모두 소모한 상태
# 2. 모든 애니를 다 본 상태
# 3. 볼 수 있는 애니 중, 그 어느것도 남은 M시간 안에 볼 수 없는 상태
# '''
# while(M > 0 and len(N_arr) > 0 and N_arr[0] <= M):
    
#     if M < (N_arr[-1]) : # 가장 긴 애니가 M보다 크면 어차피 못보니까 리스트에서 삭제
#         del N_arr[-1]

#     else: # 가장 긴 애니가 M보다 작거나 같아서 볼 수 있는 경우
#         if len(N_arr) <= K: # 한 번에 묶어서 볼 수 있는 애니의 개수보다 남은 애니가 적은 경우
#             cnt += len(N_arr) # 남은거 싹다 보면 끝
#             break
#         else:
#             M -= N_arr[-1] # 가장 긴 애니의 소요시간만큼 차감
#             cnt += K # K개를 묶어서 봤으니 cnt += K
#             del N_arr[-K :] # 본 애니만큼 묶어서 차감

# print(cnt)

'''
위 방법은 오류를 범하고 있음
ex) N,M,K = 5,15,3  // N_arr = [15,10,5,1,1]

가장 많이 볼 수 있는 경우의 수는 [10,5,1] + [1] or [1,1,5] + [10] 으로 4이지만
위 코드는 [15,10,5]로 3을 출력함.

* 그리디 알고리즘 *
현재 상황에서 지금 당장 좋은 것만 고르는 방법.
해당 알고리즘은 '정당성 분석'이 중요하다.
 = 단순히 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토해야 함.

 내가 범한 오류 : 단순히 매 상황에서 가장 큰 값만 채택함.
 
 예상 해결 방법
 1. 큰 값부터 체크 vs 작은 값부터 체크 경우의 수를 각각 재귀를 통해 돌려보고
 2. 각각의 기저사례에서 총 열람한 애니 개수를 return하여 결과 배열에 담음
 3. 배열의 최대값 출력

'''

# import sys
# sys.setrecursionlimit(10**9) # 최악에 10**9번 재귀를 호출함
# input = sys.stdin.readline

# N,M,K = map(int,input().split())

# N_arr = list(map(int,input().split()))

# N_arr.sort()

# result = []

# '''
# 기저사례
# 1. 애니를 볼 수 있는 시간 M을 모두 소모한 상태
# 2. 모든 애니를 다 본 상태
# 3. 볼 수 있는 애니 중, 그 어느것도 남은 M시간 안에 볼 수 없는 상태
# '''
# def greedy(M_,N_arr_,cnt_):
#     global result
    
#     if N_arr_[0] > M_ or M_ <= 0 or len(N_arr_) <= 0: # 기저사례
#         result.append(cnt_)
#         return
    
#     else:
#         while(N_arr_[-1] > M_): # 어차피 못보는 애니 삭제 작업
#             del N_arr_[-1]
        
#         # Case 1. 소요시간이 큰 애니부터 묶어서 시청

#         # 볼 애니 리스트가 모두 M보다 작거나 같은데, 개수가 K보다 작다면 걍 다 보는게 최선의 케이스임
#         if len(N_arr_) < K: 
#             cnt_ += len(N_arr_)
#             result.append(cnt_)
#             return
#         else:
#             greedy(M_ - N_arr_[-1], N_arr_[0 : len(N_arr_) - K + 1], cnt_ + K)
#             min_count = N_arr_.count(N_arr_[0])
#             greedy(M_ - N_arr_[0], N_arr[min_count:], cnt_ + min_count)
#         # Case 2. 소요시간이 가장 작은 애니 시청

# greedy(M,N_arr,0)

# print(max(result)) # 도출 가능한 경우의 수 중, 가장 애니를 많이보는 경우의 수 출력

'''
위의 방법은 시간초과
애초에 재귀를 10**9번까지 돌릴 수 있다는 점에서부터 에반데 싶었음

해결 방법 참고 : https://velog.io/@cjkangme/%EB%B0%B1%EC%A4%80-27313.-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98-%EA%B0%90%EC%83%81-%ED%8C%8C%EC%9D%B4%EC%8D%AC

방안 : 앞에서부터 볼 애니의 개수를 1개씩 늘려가며, 최소 M시간 안에 볼 수 있는 케이스까지 연산을 해보자.
0번째 애니부터 시작하여, 만약 i번째 애니까지 보는데 최소 M 이하의 시간이 걸렸는데, i+1번째 애니까지 보는데 M 초과하는 시간이 걸리면 답은 i+1(개)이다.

ex) 1 2 3 4 5 11 12 13 14 15
K가 2이고 M이 16이라 가정

    <앞에서부터 산정>                                                   <뒤에서부터 산정> 
case : [1] : 최소 소요시간 1                                     case : [15] : 최소 소요시간 15
case : [1,2] : 최소 소요시간 2                                   case : [14,15] : 최소 소요시간 15
case : [1,2,3] : 최소 소요시간 1 + 3 = 4                         case : [13,14,15] : 최소 소요시간 15 + 13 = 28 > M  :: 최대로 볼 수 있는 애니 수 : 2개
case : [1,2,3,4] : 최소 소요시간 : 2 + 4 = 6
case : [1,2,3,4,5] : 최소 소요시간 : 1 + 3 + 5 = 9
case : [1,2,3,4,5,11] : 최소 소요시간 : 2 + 4 + 11 = 17 > M :: 최대로 볼 수 있는 애니 수 : 5개


알 수 있는 규칙성 : 인덱스(idx)가 K보다 작을 땐, dp[idx] 에 N_arr[idx]로 초기값 선언해주고(K 범위 안으로 묶이기에 가능한 규칙), 
                   idx가 K보다 크거나 같다면 dp[idx]는 dp[idx - K] 값에서 N_arr[idx]를 더한 값과 같다.

'''
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

N_arr = list(map(int,input().split()))

N_arr.sort()

'''
M보다 큰 요소 삭제부분은 뺐음.
근거 : 어차피 메인연산 과정에서는 요소가 작은 값부터 체크하기에, 총 최소 소요시간이 M보다 커진 시점부턴 연산을 멈추기 때문

while(N_arr[-1] > M):
    del N_arr[-1]
'''

dp = []


for idx in range(N):
    if N_arr[idx] > M: # 한 애니 소요시간이 M보다 이미 커버리면 더이상 연산을 진행할 필요 X
        break

    if idx < K: # idx가 K보다 작은 부분의 dp는 N_arr[idx] 값을 삽입하여 초기값 선언.
        dp.append(N_arr[idx])

    elif dp[idx-K] + N_arr[idx] > M: # N_arr[idx] 까지의 애니를 봤을 때, 최소 소요시간이 M보다 크다면 더이상 연산을 진행할 필요 X
        break

    else: # 규칙성에 의해 dp[idx] = dp[idx-K] + N_arr[idx]
        dp.append(dp[idx-K] + N_arr[idx])

print(len(dp)) # len(dp)개의 애니를 보는 최소 소요시간은 dp[-1]일 것이다.
               # M 시간 동안 볼 수 있는 최대한의 애니메이션 개수를 세는 것이기에 dp의 길이를 출력하면 된다.