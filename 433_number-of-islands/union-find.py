'''
=> Union Find(with path compression)

Time: O(row * col)

Note: the find function takes O(lg*n), where lg*n is always smaller than 5(inverse ackermann function)

'''
class UnionFind:
    def __init__(self, rows, cols):
        self.parent = {}
        
        for row in range(rows):
            for col in range(cols):
                self.parent[(row, col)] = (row, col)
    
    def find(self, indices):
        root = indices
        while root != self.parent[root]:
            root = self.parent[root]
            
        p = indices
        while p != self.parent[p]:
            new_p = self.parent[p]
            self.parent[p] = root
            p = new_p
            
        return root
        
    def connect(self, indices1, indices2):
        p1 = self.find(indices1)
        p2 = self.find(indices2)
        
        if p1 != p2:
            self.parent[p1] = p2
            self.total -= 1
        
    def set_total(self, total):
        self.total = total
        
    def query(self):
        return self.total
    
        
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
        
        uf = UnionFind(rows, cols)
        total = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total += 1       
        uf.set_total(total)
      
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if row < rows - 1 and grid[row + 1][col] == 1:
                        uf.connect((row, col), (row + 1, col))
                    if col < cols - 1 and grid[row][col + 1] == 1:
                        uf.connect((row, col), (row, col + 1))

        
        return uf.query()
        
        