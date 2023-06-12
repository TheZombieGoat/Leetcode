"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = 1
        mr = 0
        ml = 0
        index_1 = 0
        index_2 = 0
        m = 0
        for j in range(j,len(height)):
            if height[j] + j >= mr:
                mr = height[j]
                index_2 = j
        print(mr,index_2)
        for i in range(len(height)-1):
            if min(mr,height[i])*(index_2 - i) > m:
                m = min(mr,height[i])*(index_2 - i)
                print(m)
        return m
