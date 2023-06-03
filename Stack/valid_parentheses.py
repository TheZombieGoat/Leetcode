"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        arr = [0]
        for c in s:
            if c == '{' or c == '(' or c == '[':
                arr.insert(0,c)
            elif c == ')':
                if arr[0] == '(':
                    arr.pop(0)
                else:
                    return False
            elif c == ']':
                if arr[0] == '[':
                    arr.pop(0)
                else:
                    return False
            elif c == '}':
                if arr[0] == '{':
                    arr.pop(0)
                else:
                    return False
        return len(arr) == 1
