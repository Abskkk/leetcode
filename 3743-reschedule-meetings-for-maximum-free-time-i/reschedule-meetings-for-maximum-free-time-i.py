class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeTime = []
        freeTime.append(startTime[0])
        for i in range(len(startTime) - 1):
            freeTime.append(startTime[i + 1] - endTime[i])
        freeTime.append(eventTime - endTime[-1])
        prefix = [0]
        curr = 0
        for time in freeTime:
            curr += time
            prefix.append(curr)
        res = 0
        for i in range(len(freeTime) - k):
            res = max(res, prefix[i + k + 1] - prefix[i])
        return res