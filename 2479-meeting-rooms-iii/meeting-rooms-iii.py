class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        minHeap = []
        count = [0] * n
        canUse = [True] * n
        canFind = False
        for i in range(len(meetings)):
            start, end = meetings[i][0], meetings[i][1]
            while minHeap and minHeap[0][0] <= start:
                e, room = heapq.heappop(minHeap)
                canUse[room] = True
            canFind = False
            for j in range(n):
                if canUse[j]:
                    canUse[j] = False
                    heapq.heappush(minHeap, [end, j])
                    count[j] += 1
                    canFind = True
                    break
            if not canFind:
                prevEnd, room = heapq.heappop(minHeap)
                heapq.heappush(minHeap, [end - start + prevEnd, room])
                count[room] += 1

        res = -1
        maxCount = -1
        for i in range(n):
            if count[i] > maxCount:
                res = i
                maxCount = count[i]
        return res