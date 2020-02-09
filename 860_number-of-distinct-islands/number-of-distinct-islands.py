'''
=> BFS

Time: O(row * col)
Space: O(row * col)
'''
from collections import deque
class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        
        res = set()
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                self.bfs(grid, row, col, res)
        
        return len(res)
    
    def bfs(self, grid, row, col, res):
        grid[row][col] = 0
        queue = deque([(row, col)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        points = []
        while queue:
            cur_row, cur_col = queue.popleft()
            for dx, dy in directions:
                new_row = cur_row + dx
                new_col = cur_col + dy
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 0
                    points.append((new_row - row, new_col - col))
                    queue.append((new_row, new_col))
        
        res.add(tuple(points))