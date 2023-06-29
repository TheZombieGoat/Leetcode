"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
"""

class Solution:
    def insert(self, arr: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not arr:
            arr.append(newInterval)
            return arr
        #inserting and modding intervals.
        if newInterval[0] < arr[0][0]:
            arr.insert(0,newInterval)
        else:
            i = 0
            while i < len(arr) and newInterval[0] > arr[i][0]:
                i += 1
            arr.insert(i,newInterval)
        #merging the intervals
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
