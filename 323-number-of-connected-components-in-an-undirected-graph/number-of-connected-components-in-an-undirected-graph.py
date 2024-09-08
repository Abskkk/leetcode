class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            for node in graph[i]:
                dfs(node)
    
        graph = defaultdict(list)
        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res