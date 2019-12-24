'''
Time: O(n!)
Space: O(n)
'''
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
=> BFS Non-recursive

enque board into queue
every loop add a queen to all board in queue
get the result
""" 
from collections import deque
import copy
class Solution2:
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
            for _ in range(size):
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
        

"""
=> Top-Down DFS
We don't need to store an entire board, we just need to store the information of Q and reconstruct the board once we are done

We use a list to record the queen's col pos in each row, it will be a list like
[2, 1, 0] 
 0  1  2

"""
import copy
class Solution3:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []
        
        self.pos_lists = []
        self.dfs(n, 0, [])
        res = []
        for pos_list in self.pos_lists:
            res.append(self.draw_board(pos_list, n))
        
        return res
        
    def dfs(self, n, placed, pos_list):
        if n == placed:
            self.pos_lists.append(copy.copy(pos_list))
            
        for i in range(n):
            if self.valid_pos(i, pos_list):
                pos_list.append(i)
                self.dfs(n, placed + 1, pos_list)
                pos_list.pop()
                
    def valid_pos(self, col_index, pos_list):
        # vertical
        if col_index in pos_list:
            return False
        
        new_row = len(pos_list)   
        new_col = col_index
        for row_index in range(len(pos_list)):
            if abs(row_index - new_row) == abs(pos_list[row_index] - new_col):
                return False
            
        return True
    
    def draw_board(self, pos_list, n):
        res = []
        
        for col_index in pos_list:
            tmp_res = ['.' if i != col_index else 'Q' for i in range(n) ]
            tmp_res = ''.join(tmp_res)
            res.append(tmp_res)
            
        return res
        
"""
=> Bottom-Up DFS
We don't need to store an entire board, we just need to store the information of Q and reconstruct the board once we are done

We use a list to record the queen's col pos in each row, it will be a list like
[2, 1, 0] 
 0  1  2

"""
import copy
class Solution4:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []
        
        self.pos_lists = []
        self.pos_lists = self.dfs(n, 0, [])
        res = []
        for pos_list in self.pos_lists:
            res.append(self.draw_board(pos_list, n))
        
        return res
        
    def dfs(self, n, placed, pos_list):
        results = []
        
        if n == placed:
            results.append(copy.copy(pos_list))
            return results
            
        for i in range(n):
            if self.valid_pos(i, pos_list):
                pos_list.append(i)
                tmp_res = self.dfs(n, placed + 1, pos_list)
                if tmp_res: 
                    print(tmp_res)
                    for res in tmp_res:
                        results.append(res)
                pos_list.pop()
        
        return results
                
    def valid_pos(self, col_index, pos_list):
        # vertical
        if col_index in pos_list:
            return False
        
        new_row = len(pos_list)   
        new_col = col_index
        for row_index in range(len(pos_list)):
            if abs(row_index - new_row) == abs(pos_list[row_index] - new_col):
                return False
            
        return True
    
    def draw_board(self, pos_list, n):
        res = []
        
        for col_index in pos_list:
            tmp_res = ['.' if i != col_index else 'Q' for i in range(n) ]
            tmp_res = ''.join(tmp_res)
            res.append(tmp_res)
            
        return res

'''
=> Bottom-up DFS
'''
import copy
class Solution5:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        res = self.dfs(n, 0)
        boards = []
        for cols in res:
            boards.append(self.build_res(n, cols))
        
        return boards
        
    def dfs(self, n, row):
        res = []
        if row == n:
            return [[]]
    
        results = self.dfs(n, row + 1)
        for tmp_res in results:
            for i in range(n):
                if self.valid(n, row, i, tmp_res):
                    tmp_copy = [i] + copy.copy(tmp_res)
                    res.append(tmp_copy)
        return res
                
        
    def valid(self, n, row_index, col_index, cols):
        if col_index in cols:
            return False
            
        for row, col in enumerate(cols):
            if abs(row + 1) == abs(col - col_index):
                return False
                
        return True

    def build_res(self, n, cols):
        res = []
        
        for col in cols:
            res.append(''.join(['Q' if i == col else '.' for i in range(len(cols))]))
        return res 