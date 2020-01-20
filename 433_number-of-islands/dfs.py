'''
=> DFS

Time: O(row * col)
Space: O(row * col)

'''
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
                    self.dfs(grid, row, col)
                    count += 1
                    
        return count
        
    def dfs(self, grid, row, col):
        drow = [1, -1, 0, 0]
        dcol = [0, 0, 1, -1]
        
        grid[row][col] = 0
        for i in range(4):
            new_row = row + drow[i]
            new_col = col + dcol[i]
            if self.valid(grid, new_row, new_col):
                grid[new_row][new_col] = 0
                self.dfs(grid, new_row, new_col)
                
    def valid(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return False
            
        if col < 0 or col >= len(grid[0]):
            return False
            
        if grid[row][col] == 0:
            return False
            
        return True