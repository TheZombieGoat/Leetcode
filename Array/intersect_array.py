#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution(object):
    def intersect(self, nums1, nums2):
        i = 0
        j = 0
        arr = []
        if len(nums1) <= len(nums2):
            small = sorted(nums1)
            big = sorted(nums2)
        else:
            small = sorted(nums2)
            big = sorted(nums1)
        while j < len(small) and i < len(big):
            if small[j] < big[i]:
                j += 1
            elif small[j] == big[i]:
                arr.append(small[j])
                j += 1
                i += 1
            else:
                 i += 1
        return arr