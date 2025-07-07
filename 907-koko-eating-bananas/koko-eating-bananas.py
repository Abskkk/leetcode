class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if helper(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo