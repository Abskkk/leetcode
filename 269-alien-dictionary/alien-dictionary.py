class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in graph}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if word1[:minLen] == word2[:minLen] and len(word1) > len(word2):
                return ""
            for i in range(minLen):
                if word1[i] != word2[i]:
                    if word2[i] not in graph[word1[i]]:
                        graph[word1[i]].add(word2[i])
                        indegree[word2[i]] += 1
                    break
        visited = {}
        res = []
        def dfs(ch):
            if ch in visited:
                return visited[ch]
            visited[ch] = True
            for neighbor in graph[ch]:
                if dfs(neighbor):
                    return True
            visited[ch] = False
            res.append(ch)
            return False
        for ch in graph:
            if dfs(ch):
                return ""
        res.reverse()
        return ''.join(res)
