import copy
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    
    """
    dfs search for all result, if n queens can be places, save the result
    for placing 1 queen, we need to test if cur pos is a valid pos
    
    for each row, we check all n positions, if either one is valid, we record current result and put queen into corresponding position
    
    XXX
    XOX
    XXX
    """
    
    def solveNQueens(self, n):
        # write your code here
        if n == 0:
            return []
            
        board = [['.' for i in range(n)] for j in range(n)]
        self.res = []
        self.dfs(n, n, board)
        
        return self.res
        
    def dfs(self, n, remain_queens, board):
        if remain_queens == 0:
            self.res.append(list([''.join(board[i]) for i in range(n)]))
            return
        
        for i in range(n):
            row = n - remain_queens
            col = i
            if self.valid_pos(board, n, row, col):
                board[row][col] = 'Q'
                self.dfs(n, remain_queens - 1, board)
                board[row][col] = '.'
                
    def valid_pos(self, board, n, row, col):
        # col
        for i in range(n):
            if i != row and board[i][col] == 'Q':
                return False
                
        # diagonal
        dx = [-1, 1, 1, -1]
        dy = [-1, 1, -1, 1]
        for i in range(4):
            tmp_row = row + dx[i]
            tmp_col = col + dy[i]
            while tmp_row < n and tmp_row >= 0 and tmp_col < n and tmp_col >= 0:
                if board[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row += dx[i]
                tmp_col += dy[i]
        
        return True
                  
"""
    BFS Non-recursive
    
    enque board into queue
    every loop add a queen to all board in queue
    get the result
    """ 
from collections import deque
import copy
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        
        if n == 0:
            return []
            
        board = [['.' for i in range(n)] for j in range(n)]
        queue = deque([board])
        
        row = 0
        queen_count = n
        while queen_count > 0:
            size = len(queue)
            for i in range(size):
                cur_board = queue.popleft()
                for j in range(n):
                    col = j
                    if self.valid_pos(cur_board, n, row, col):
                        cur_board[row][col] = 'Q'
                        queue.append(copy.deepcopy(cur_board))
                        cur_board[row][col] = '.'
            row += 1
            queen_count -= 1
            
        results = []
        while queue:
            board = queue.pop()
            results.append(list([''.join(row) for row in board]))
        
        return results
        
    def valid_pos(self, board, n , row, col):
        # col
        for i in range(n):
            if i != row and board[i][col] == 'Q':
                return False
                
        dx = [1, -1, 1, -1]
        dy = [1, 1, -1, -1]
        for i in range(4):
            tmp_row = row + dx[i]
            tmp_col = col + dy[i]
            while tmp_row >= 0 and tmp_row < n and tmp_col >= 0 and tmp_col < n:
                if board[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row += dx[i]
                tmp_col += dy[i]
                
                
        return True
        