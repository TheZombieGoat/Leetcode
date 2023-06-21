"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for x in magazine:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for x in ransomNote:
            if x in d and d[x] > 0:
                d[x] -= 1
            else:
                return False
        return True
