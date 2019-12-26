"""
Input:	[[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
Output: [1,2,3,6,9,8,7,4,5]

1 2 3   123698745  
4 5 6
7 8 9

0, 0 - 0, 1 - 0, 2 - 1, 2 - 2, 2 - 2, 1 - 2, 0 - 1, 0

start from 0, 0
move m - 1 right on x
move n - 1 down on y
move m - 1 left on x
move n - 2 up on y

"""

class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        if not matrix:
            return[]
            
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
    
        row_start = 0
        row_end = m
        col_start = 0
        col_end = n
        
        count = 0
        while count < m * n:
            # left-right
            for i in range(col_start, col_end):
                res.append(matrix[row_start][i])
                count += 1
                
            # top-bottom
            for i in range(row_start + 1, row_end):
                res.append(matrix[i][col_end - 1])
                count += 1
            
            if row_start + 1 == row_end: break
            # right-left
            for i in range(col_end - 2, col_start - 1, -1):
                res.append(matrix[row_end - 1][i])
                count += 1
                
            if col_start + 1 == col_end: break
            # bottom-top
            for i in range(row_end - 2, row_start, -1):
                res.append(matrix[i][col_start])
                count += 1
            
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
            
        return res
                