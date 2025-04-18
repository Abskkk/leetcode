class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if high < 0:
                return False
            low = 0 if low < 0 else low
        return low == 0