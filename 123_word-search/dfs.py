class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not board:
            return False
            
        if not word:
            return True
            
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if self.dfs(board, row, col, word, 0):
                    return True
                    
        return False
        
    def dfs(self, board, row, col, word, index):
        if index == len(word):
            return True
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
            
        if word[index] != board[row][col]:
            return False
            
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        board[row][col] = '@'
        for drow, dcol in DIRECTIONS:
            new_row = row + drow
            new_col = col + dcol
            if self.dfs(board, new_row, new_col, word, index + 1):
                return True
        board[row][col] = word[index]
                
        return False
            
