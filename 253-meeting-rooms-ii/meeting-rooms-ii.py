class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        room = 0
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, end)
            else:
                heapq.heappush(minHeap, end)
                room += 1
        return room