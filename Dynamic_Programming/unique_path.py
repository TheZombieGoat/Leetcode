"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:    
    def uniquePaths(self,m: int, n: int) -> int:
        return up(m,n)
d = {}
def up(a,b):
    if a == 1 or b == 1:
        return 1 
    else:
        if (a,b) in d:
            return d[(a,b)]
        else:
            val = up(a-1,b) + up(a,b-1) 
            d[(a,b)] = val
            return val


