class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        SINGLE_STEP_MOVES = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),  # Adjacent moves (right, left, down, up)
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),  # Diagonal moves
                (-2, 1),
                (-2, -1),
                (2, 1),
                (2, -1),  # Extended moves (knight-like moves)
                (1, -2),
                (-1, -2),
                (1, 2),
                (-1, 2),
            ]
        SKIP_DOT_MOVES = [
                (0, 2),
                (0, -2),
                (2, 0),
                (-2, 0),  # Straight skip moves (e.g., 1 to 3, 4 to 6)
                (-2, -2),
                (2, 2),
                (2, -2),
                (-2, 2),  # Diagonal skip moves (e.g., 1 to 9, 3 to 7)
            ]
        visited = set()
        count = 0
        def backtrack(i, j, visited, path_len):
            nonlocal count
            if not (0 <= i < 3 and 0 <= j < 3) or (i,j) in visited:
                return
            
            if m <= path_len <= n:
                count += 1
            
            if path_len == n:
                return

            visited.add((i,j))
            for r, c in SINGLE_STEP_MOVES:
                nr, nc = i + r, j + c
                backtrack(nr, nc, visited, path_len + 1)
            for r, c in SKIP_DOT_MOVES:
                nr, nc = i + r, j + c
                cr, cc = (i+nr)//2, (j+nc)//2
                if (cr, cc) in visited:
                    backtrack(nr, nc, visited, path_len + 1)
            visited.remove((i,j))

        for i in range(3):
            for j in range(3):
                backtrack(i,j,visited,1)
        return count
