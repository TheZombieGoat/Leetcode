"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
#Single pass solution with constant extra space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        if n == 1:
            return nums
        i,j,k = 0,0,n-1
        while j < n:
            while i < n and nums[i] == 0:
                i += 1
            while k > 0 and nums[k] == 2:
                k -= 1
            if nums[j] == 2 and j < k:
                nums[k],nums[j] = nums[j],nums[k]     
                k -= 1
            if nums[j] == 0 and j > i:
                nums[i],nums[j] = nums[j],nums[i]          
                i += 1 
            j += 1
