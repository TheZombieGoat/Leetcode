# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# O(n) time complexity, O(1) space complexity.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k  %= size
        if k != 0:
            nums.reverse() 
            a = (size - k) // 2
            for i in range(a):
                nums[k+i],nums[-i-1] = nums[-i-1],nums[k+i]
            for i in range(k//2):
                nums[i],nums[k-i-1] = nums[k-i-1],nums[i]
