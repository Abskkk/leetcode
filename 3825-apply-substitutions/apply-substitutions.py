class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replacementsMap = {}
        for k, v in replacements:
            replacementsMap[k] = v
        cache = {}
        def dfs(text):
            if text in cache:
                return cache[text]
            res = []
            index = 0
            while index < len(text):
                if text[index] != '%':
                    res.append(text[index])
                    index += 1
                else:
                    replacedText = replacementsMap[text[index + 1]]
                    resolvedText = dfs(replacedText)
                    res.append(resolvedText)
                    index += 3
            return ''.join(res)
        return dfs(text)