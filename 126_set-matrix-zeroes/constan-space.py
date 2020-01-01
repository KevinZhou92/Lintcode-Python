'''
Time: O(mn)
Space: O(1)
'''
    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return [[]]
        row_zero = False
        col_zero = False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(cols):
            if matrix[0][i] == 0:
                row_zero = True
        
        for i in range(rows):
            if matrix[i][0] == 0:
                col_zero = True
                
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if row_zero:
            for i in range(cols):
                matrix[0][i] = 0
                
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        return matrix