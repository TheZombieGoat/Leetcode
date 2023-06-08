"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for x in t:
            if x not in d:
                return False
            else:
                d[x] -= 1
                if d[x] < 0:
                    return False
        return True
