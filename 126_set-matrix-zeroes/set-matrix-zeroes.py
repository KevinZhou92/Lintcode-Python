'''
Time: O(mn)
Space: O(m + n)
'''
class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return [[]]
            
        zero_rows = set()
        zero_cols = set()
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in zero_rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
                
        for col in zero_cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
                
        return matrix