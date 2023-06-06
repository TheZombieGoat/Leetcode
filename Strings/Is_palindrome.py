"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i,j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True
