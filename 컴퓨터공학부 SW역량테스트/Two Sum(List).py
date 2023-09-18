# https://leetcode.com/problems/two-sum/submissions/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,3],6))
