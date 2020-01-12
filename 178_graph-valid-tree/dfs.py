'''
=> DFS
Time: O(n)
'''
from collections import *
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
        
        neighbors = self.get_neighbors(edges)
        visited = set([0])
        self.dfs(0, visited, neighbors)
        
        return len(visited) == n
    
    def dfs(self, node, visited, neighbors):
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, visited, neighbors)
        
    def get_neighbors(self, edges):
        neighbors = defaultdict(list)
        
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
            
        return neighbors
