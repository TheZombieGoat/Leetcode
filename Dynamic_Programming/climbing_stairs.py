"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        s = [0]*n
        s[0] = 1
        s[1] = 2
        for i in range(2,n):
            s[i] = s[i-2] + s[i-1]
        return s[n-1]
