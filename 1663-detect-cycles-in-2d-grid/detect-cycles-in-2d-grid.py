class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(row, col, prevRow, prevCol):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != grid[prevRow][prevCol]:
                return False
            if (row, col) in visited:
                return True
            visited.add((row, col))
            direction = [[1,0],[0,1],[-1,0],[0,-1]]
            for offsetRow, offsetCol in direction:
                newRow, newCol = row + offsetRow, col + offsetCol
                if newRow == prevRow and newCol == prevCol:
                    continue
                if dfs(newRow, newCol, row, col):
                    return True
            
            return False
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and dfs(i, j, i, j):
                    return True
        return False

