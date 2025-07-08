class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval[0], newInterval[1]
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            currStart, currEnd = intervals[i][0], intervals[i][1]
            # not overlap
            if currEnd < newStart:
                res.append([currStart, currEnd])
            elif currStart > newEnd:
                res.append([newStart, newEnd])
                res += intervals[i:]
                return res
            # overlap
            else:
                newStart = min(currStart, newStart)
                newEnd = max(currEnd, newEnd)
        res.append([newStart, newEnd])
        return res
