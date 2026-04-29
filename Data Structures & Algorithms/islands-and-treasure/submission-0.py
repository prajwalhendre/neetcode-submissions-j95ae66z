from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, columns = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    queue.append((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    
        
        #can add in other nodes while in queue and track them too

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < rows and nr >= 0 and nc < columns and nc >= 0 and grid[nr][nc] == 2147483647):
                    queue.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
