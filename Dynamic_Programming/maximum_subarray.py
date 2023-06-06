#Given an integer array nums, find the subarray with the largest sum, and return its sum.

import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = maxiSum = -sys.maxsize
        for i in nums:
            maxiSum = max(maxiSum+i, i)
            maxSum = max(maxSum, maxiSum)
        return maxSum
