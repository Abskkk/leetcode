class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        # push a, b, c in heap
        if a != 0: heapq.heappush(maxHeap, (-a, 'a'))
        if b != 0: heapq.heappush(maxHeap, (-b, 'b'))
        if c != 0: heapq.heappush(maxHeap, (-c, 'c'))

        charArray = []
        while maxHeap:
            if len(charArray) <= 1 or (charArray[-1] != charArray[-2] or charArray[-1] != maxHeap[0][1]):
                count, currChar = heapq.heappop(maxHeap)
                charArray.append(currChar)
                # negative number for maxHeap
                count += 1
                if count < 0:
                    heapq.heappush(maxHeap, (count, currChar))
            else:
                tempCount, tempChar = heapq.heappop(maxHeap)
                if not maxHeap:
                    break
                count, currChar = heapq.heappop(maxHeap)
                charArray.append(currChar)
                # negative number for maxHeap
                count += 1
                if count < 0:
                    heapq.heappush(maxHeap, (count, currChar)) 
                heapq.heappush(maxHeap, (tempCount, tempChar))
        return ''.join(charArray)