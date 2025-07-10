class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i][0], intervals[i][1]
            if currStart < prevEnd:
                count += 1
                prevEnd = min(prevEnd, currEnd)
            else:
                prevEnd = currEnd
        return count
