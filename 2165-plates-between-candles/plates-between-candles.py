class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        leftIndex, rightIndex = [-1] * n, [-1] * n
        prefixSum = [0] * n
        plates = 0
        for i in range(len(s)):
            if s[i] == '*':
                plates += 1
            prefixSum[i] = plates
            if s[i] == '|':
                leftIndex[i] = i
            elif i > 0:
                leftIndex[i] = leftIndex[i - 1]
        for j in range(n - 1, -1, -1):
            if s[j] == '|':
                rightIndex[j] = j
            elif j < n - 1:
                rightIndex[j] = rightIndex[j + 1]
        res = []
        for left, right in queries:
            rightCandle, leftCandle = rightIndex[left], leftIndex[right]
            if rightCandle == -1 or leftCandle == -1 or leftCandle < rightCandle:
                res.append(0)
            else:
                res.append(prefixSum[leftCandle] - prefixSum[rightCandle])
        return res