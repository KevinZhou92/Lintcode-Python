'''
=> DFS
find entry in map, search continuously
Time: O(m * n * 4^l), m is the length of the board and n is the width of the board and l is the average length of the word
Space: O(l)
'''
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, visited, i, j, 0, word):
                    return True
                    
        return False
        
    def dfs(self, board, visited, row, col, char_index, word):
        if board[row][col] != word[char_index]:  
            return False
            
        if char_index == len(word) - 1:
            return True
        
        visited[row][col] = 1
        
        if self.is_valid(board, row - 1, col) and visited[row - 1][col] != 1:
            visited[row - 1][col] = 1
            if self.dfs(board, visited, row - 1, col, char_index + 1, word):
                return True
            visited[row - 1][col] = 0
        
        if self.is_valid(board, row + 1, col) and visited[row + 1][col] != 1:
            visited[row + 1][col] = 1
            if self.dfs(board, visited, row + 1, col, char_index + 1, word):
                return True
            visited[row + 1][col] = 0
        
        if self.is_valid(board, row, col + 1) and visited[row][col + 1] != 1:
            visited[row][col + 1] = 1
            if self.dfs(board, visited, row, col + 1, char_index + 1, word):
                return True
            visited[row][col + 1] = 0
            
        if self.is_valid(board, row, col - 1) and visited[row][col - 1] != 1:
            visited[row][col - 1] = 1
            if self.dfs(board, visited, row, col - 1, char_index + 1, word):
                return True
            visited[row][col - 1] = 0
        
        visited[row][col] = 0   
            
        return False
        
    def is_valid(self, board, row, col):
        
        rows = len(board)
        cols = len(board[0])
        
        if row < 0 or row >= rows:
            return False
            
        if col < 0 or col >= cols:
            return False
            
        return True

