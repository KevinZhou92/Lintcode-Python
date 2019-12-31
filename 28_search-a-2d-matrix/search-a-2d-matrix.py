'''
=> Binary Search
Time: O(logn + logm)
Space: O(1)
'''
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        row_index = self.col_search(matrix, rows, cols, target)
        if row_index == -1 or self.row_search(matrix, row_index, cols, target) == -1:
            return False
            
        return True
    
    def row_search(self, matrix, row_index, cols, target):
        start, end = 0, cols - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[row_index][mid] > target:
                end = mid
            else:
                start = mid
                
        if matrix[row_index][end] == target:
            return end
            
        if matrix[row_index][start] == target:
            return start
            
        return -1
        
    def col_search(self, matrix, rows, cols, target):
        start, end = 0, rows - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][cols - 1] < target:
                start = mid
            else:
                end = mid
        
        if matrix[end][cols - 1] < target:
            return -1
        if matrix[start][cols - 1] >= target:
            return start
        
        return end