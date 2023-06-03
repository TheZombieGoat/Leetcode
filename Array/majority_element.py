#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than (n / 2) times. You may assume that the majority element always exists in the array.

 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        m = 0
        res = 0
        if len(nums) < 3:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                counter += 1
            else:
                counter = 0
            if counter > m:
                m = counter
                res = nums[i]
        return res
