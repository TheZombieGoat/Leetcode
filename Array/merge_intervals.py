"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        i, j, size = 0, 1, len(arr)
        starter, ender = arr[0][0], arr[0][1]
        while j < size:
            if arr[i][1] >= arr[j][0]:
                if arr[j][1] > arr[i][1]:
                    arr[i][1] = arr[j][1]
                arr.pop(j)
                size -= 1
            elif arr[i][1] < arr[j][0]:
                j += 1
                i += 1
        return arr
