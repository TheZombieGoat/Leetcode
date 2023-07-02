"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

#O(n) time complexity and O(n) space complexity.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        total = 0
        temp = 0
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for k in d:
            if d[k] >= 2:
                if d[k] % 2 == 0:
                    total += d[k]
                else:
                    total += d[k] - 1
                    temp = 1
            else:
                temp = 1
        return total + temp
