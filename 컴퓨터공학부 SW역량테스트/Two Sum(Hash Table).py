# https://leetcode.com/problems/two-sum/submissions/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], idx]
            nums_dict[num] = idx
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,3], 6))