class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        # write your code here
        if not board:
            return True
        rows = len(board)
        cols = len(board[0])
        
        return self.check_row(board, rows, cols) and self.check_col(board, rows, cols) and self.check_square(board, rows, cols)
        
    def check_row(self, board, rows, cols):
        for i in range(rows):
            numbers = set()
            for j in range(cols):
                if not self.is_valid(board[i][j], numbers):
                    return False    
                numbers.add(board[i][j])
                    
        return True
        
    def check_col(self, board, rows, cols):
        for i in range(cols):
            numbers = set()
            for j in range(rows):
                if not self.is_valid(board[j][i], numbers):
                    return False
                numbers.add(board[j][i])
            
        return True    
                
    def check_square(self, board, rows, cols):
        for row in range(0, rows - 2, 3):
            for col in range(0, cols - 2, 3):
                numbers = set()
                for k in range(1, 10):
                    row_index = row + (k - 1) // 3
                    col_index = col + (k - 1) % 3
                    if not self.is_valid(board[row_index][col_index], numbers):
                        return False    
                    numbers.add(board[row_index][col_index])
                    
        return True
        
    def is_valid(self, char, numbers):
        if char != '.' and not char.isdigit():
            return False
        
        if char != '.' and char in numbers:
            return False
            
        return True
    
