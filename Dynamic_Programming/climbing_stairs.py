"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        i,j = 1,2
        for _ in range(2,n):
            i,j = j, i+j
        return j if n > 1 else i
