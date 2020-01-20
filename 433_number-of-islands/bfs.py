'''
=> BFS

Time: O(row * col)
Space: O(row * col)
'''
from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    self.bfs(grid, row, col)
                    count += 1
                    
        return count
        
    def bfs(self, grid, row, col):
        drow = [1, -1, 0, 0]
        dcol = [0, 0, -1, 1]
        
        queue = deque([[row, col]])
        grid[row][col] = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                for i in range(4):
                    new_row = row + drow[i]
                    new_col = col + dcol[i]
                    if self.valid(grid, new_row, new_col):
                        queue.append([new_row, new_col])
                        grid[new_row][new_col] = 0
                        
    def valid(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return False
            
        if col < 0 or col >= len(grid[0]):
            return False
            
        if grid[row][col] == 0:
            return False
            
        return True
            