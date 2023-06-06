#Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum
