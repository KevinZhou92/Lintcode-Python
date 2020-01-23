'''
=> Union Find
Time: O(n), where n is number of operators
Space: O(m*n)

1. add a new island, count + 1, check up, left, right, down
2. return final count

Note: Input might have duplicate
'''

class UnionFind:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.count = 0
        self.fathers = {(row, col): (row, col) for row in range(rows) for col in range(cols) }
        
    def find(self, indices):
        root = indices
        while root != self.fathers[root]:
            root = self.fathers[root]
        
        p = indices
        while p != self.fathers[p]:
            new_p = self.fathers[p]
            self.fathers[p] = root
            p = new_p
        
        return root
        
    def connect(self, indices1, indices2):
        father1 = self.find(indices1)
        father2 = self.find(indices2)
        
        if father1 != father2:
            self.fathers[father1] = father2
            self.count -= 1
            
    def query(self):
        return self.count
    
    def add(self):
        self.count += 1


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        if not n or not m or not operators:
            return []
        
        uf = UnionFind(n, m)
        islands = {}
        drow = [1, -1, 0, 0]
        dcol = [0, 0, -1, 1]
        res = []
        for operator in operators:
            row = operator.x
            col = operator.y
            if self.is_valid(row, col, n, m) and (row, col) not in islands:
                islands[(row, col)] = 1
                uf.add()
                for i in range(4):
                    new_row = row + drow[i]
                    new_col = col + dcol[i]
                    if self.is_valid(new_row, new_col, n, m) and (new_row, new_col) in islands:
                        uf.connect((row, col), (new_row, new_col))
            res.append(uf.query())
                        
        return res
        
    def is_valid(self, row, col, rows, cols):
        if 0 <= row < rows and 0 <= col < cols:
            return True
        
        return False
            
        
        
