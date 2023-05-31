#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

#solution using dicts. O(n) time and space.
class Solution(object):
    def intersect(self, nums1, nums2):
        d1 = {}
        d2 = {}
        arr = []
        for num in nums1:
            d1[num] = d1.get(num,0) + 1
        for num in nums2:
            d2[num] = d2.get(num,0) + 1
        for key in d1:
            if key in d2:
                arr += [key]*min(d2[key],d1[key])
        return arr
