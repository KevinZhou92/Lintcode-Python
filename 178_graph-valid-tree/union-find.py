'''
=> Union Find

Time: O(n)
Space: O(n)

'''
from collections import *
class UnionFind:
    def __init__(self, total_nodes):
        self.fathers = {index: index for index in range(total_nodes)}
        self.count = total_nodes
        
    def find(self, index):
        path = []
        while index != self.fathers[index]:
            path.append(index)
            index =  self.fathers[index]
        
        for p in path:
            self.fathers[p] = index
            
        return index
        
    def connect(self, index1, index2):
        father1 = self.find(index1)
        father2 = self.find(index2)
        
        if father1 != father2:
            self.fathers[father1] = father2
            self.count -= 1
            
    def query(self):
        return self.count
        

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        
        uf = UnionFind(n)
        neighbors = self.get_neighbors(edges)
        
        for node in neighbors:
            for neighbor in neighbors[node]:
                uf.connect(node, neighbor)

        return uf.query() == 1    

    def get_neighbors(self, edges):
        neighbors = defaultdict(list)
        
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
            
        return neighbors
