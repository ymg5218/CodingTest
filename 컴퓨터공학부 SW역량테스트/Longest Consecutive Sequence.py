# https://leetcode.com/problems/longest-consecutive-sequence/


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # 중복 제거, set 메소드로 해시테이블 기반 자료구조에 저장
        longest = 0 # 가장 길었던 길이

        for num in nums:
            if num - 1 in num_set: # O(1) 
                continue
            length = 1
            while num + length in num_set: # O(1)
                length += 1
            longest = max(length, longest) # longest, length 비교하여 더 길었던 시퀀스로 longest 갱신
        
        return longest

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))