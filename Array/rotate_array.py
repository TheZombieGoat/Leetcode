# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# O(n) time complexity, O(n) space complexity.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
