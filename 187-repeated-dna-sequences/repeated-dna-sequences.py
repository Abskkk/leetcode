class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        visited = set()
        res = set()
        for i in range(n - 9):
            curr = s[i: i + 10]
            if curr in visited:
                res.add(curr)
            else:
                visited.add(curr)
        return list(res)