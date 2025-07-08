class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heap = []
        n = len(events)
        events.sort(key=lambda x: x[0])
        maxDay = max(x[1] for x in events)
        i = 0
        res = 0
        for day in range(1, maxDay + 1):
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap and heap[0] >= day:
                heapq.heappop(heap)
                res += 1
        return res