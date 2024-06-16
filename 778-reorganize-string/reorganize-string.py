class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(maxHeap)
        res = ""
        while len(maxHeap) > 0:
            firstCnt, first = heapq.heappop(maxHeap) 
            # firstCnt here is negative
            if not res or first != res[-1]:
                res += first
                if firstCnt != -1:
                    heapq.heappush(maxHeap, (firstCnt + 1, first))
            else:
                if len(maxHeap) == 0:
                    return ""
                secondCnt, second = heapq.heappop(maxHeap)
                res += second
                if secondCnt != -1:
                    heapq.heappush(maxHeap, (secondCnt + 1, second))
                heapq.heappush(maxHeap, (firstCnt, first))
        return res