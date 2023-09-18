# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) # 입력받은 temperatures 리스트의 길이 n
        result = [0 for _ in range(n)] # Output용 결과를 담아낼 리스트 선언 및 모든 요소 0으로 초기화
        stack = [] # 스택 리스트 선언

        # temperatures 리스트를 순회하며 인덱스 번호는 day, 온도(값)는 temp에 담음
        for day, temp in enumerate(temperatures):
            # stack 리스트가 비어있지 않고, stack의 top이 temp보다 작다면 (온도가 낮다면)
            while stack and stack[-1][1] < temp:
                # temp와 stack의 top의 day 차이를 result에 기록한다.
                result[stack[-1][0]] = day - stack[-1][0]
                # 스택 pop하여 top 삭제
                stack.pop()
            # 해당 day와 temp를 stack에 push
            stack.append([day, temp])
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))

