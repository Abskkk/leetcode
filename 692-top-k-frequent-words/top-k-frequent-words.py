class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    def __lt__(self, p):
        return self.count < p.count or (self.count == p.count and self.word > p.word)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        h = []
        for word, freq in cnt.items():
            heappush(h, Pair(word, freq))
            if len(h) > k:
                heapq.heappop(h)
        return [p.word for p in sorted(h, reverse=True)]
        