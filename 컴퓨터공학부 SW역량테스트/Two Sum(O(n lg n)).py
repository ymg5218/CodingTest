# https://leetcode.com/problems/two-sum/submissions/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for idx, value in enumerate(nums):
            sorted_nums.append([idx,value])

        nums.clear()
        # 파이썬 sort 메소드 : 시간복잡도 O(n lg n)
        nums = sorted(sorted_nums, key = lambda x : x[1])

        # 투 포인터 이용
        start = 0
        end = len(nums) - 1

        # start가 end보다 작을 때까지 반복.
        while(start < end):
            if nums[start][1] + nums[end][1] > target:
                end -= 1
            elif nums[start][1] + nums[end][1] < target:
                start += 1
            else:
                return [nums[start][0], nums[end][0]]


        
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,2,4],6))