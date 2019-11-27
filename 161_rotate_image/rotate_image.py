class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        # write your code here
        """
        1 2   --> 3 1
        3 4       4 2
        
        1 2 3     7 4 1  
        4 5 6  -->8 5 2
        7 8 9     9 6 3
        
        1 2 3 4   13 9 5 1
        5 6 7 8   14 10 6 2
        9 101112  15 11 7 3
        13141516  16 12 8 4
        
        0, 0 -> 0, 2 
        0, 1 -> 1, 2
        0, 2 -> 2,  0
        1, 0 -> 0, 1
        1, 1 -> 1, 1
        1, 2 -> 2, 1
        create a new array
        copy over elem into new pos
        every elem will move
        new row = old_col
        new col = length - 1 - old_row
        """
        
        if not matrix:
            return
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        new_matrix = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                new_row = j
                new_col = rows - 1 - i
                new_matrix[new_row][new_col] = matrix[i][j]
                
                
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = new_matrix[i][j]
        
            def rotate(self, matrix):
        # write your code here
        if not matrix:
            return
    
    def rotate(self, matrix):    
    """
    1 2 3 4      13 9  5 1
    5 6 7 8  --> 14 10 6 2
    9 101112     15 11 7 3 
    13141516     16 12 8 4
    loop n // 2 times
        loop num of rows
            replace 4 elem at a time
    
    1 2 3   7 4 1
    4 5 6   8 5 2
    7 8 9   9 6 3
    
    new_row = old_col
    new_col = n - 1 - row
    """
    
    
    n = len(matrix)
    
    
    for i in range(n // 2):
        for j in range((n + 1)// 2 ):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = tmp
               