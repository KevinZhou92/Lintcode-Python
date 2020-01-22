class UnionFind:
    def __init__(self, rows, cols):
        self.parent = {}
        
        for row in range(rows):
            for col in range(cols):
                self.parent[(row, col)] = (row, col)
    
    def find(self, indices):
        root = indices
        while root != self.parent[root]:
            root = self.parent[root]
            
        p = indices
        while p != self.parent[p]:
            new_p = self.parent[p]
            self.parent[p] = root
            p = new_p
            
        return root
        
    def connect(self, indices1, indices2):
        p1 = self.find(indices1)
        p2 = self.find(indices2)
        
        if p1 != p2:
            self.parent[p1] = p2
            self.total -= 1
        
    def set_total(self, total):
        self.total = total
        
    def query(self):
        return self.total