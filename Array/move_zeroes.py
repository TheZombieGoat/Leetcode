"""
Question:

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

#Used a two-pointer approach for O(n) time complexity
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] != 0 and nums[p1] == 0:
                nums[p1],nums[p2] = nums[p2],nums[p1]
            
            if nums[p1] != 0:
                p1 += 1