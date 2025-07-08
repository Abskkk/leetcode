class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, f = -1):
            nonlocal res
            children = []
            for child in graph[node]:
                if child == f:
                    continue
                children.append(dfs(child, node))
            if not children:
                return cost[node]
            maxScore = max(children)
            for score in children:
                res += 1 if maxScore != score else 0
            return maxScore + cost[node]
        res = 0
        dfs(0)
        return res