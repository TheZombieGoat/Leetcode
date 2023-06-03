#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than (n / 2) times. You may assume that the majority element always exists in the array.

#O(n) time 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for n in nums:
            if count==0:
                result=n
            if n==result:
                count+=1
            else:
                count-=1
        return result
