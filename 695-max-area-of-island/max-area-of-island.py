class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # Base cases: out of bounds or already visited or water
            if (r < 0 or r >= m or c < 0 or c >= n or 
                grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            area = 1
            # Explore all four directions
            offset = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for offsetRow, offsetCol in offset:
                area += dfs(r + offsetRow, c + offsetCol)
            return area

        m, n = len(grid), len(grid[0])
        visited = set()  # Set to track visited cells
        maxArea = 0

        # Traverse each cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(dfs(i, j), maxArea)
                    
        return maxArea
