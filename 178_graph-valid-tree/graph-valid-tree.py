'''
=> BFS

Time: O(n)
Space: O(n)

Note:
1. Undirected Edges, we should build a mutal relationship, a->b and b->a
2. Valid Tree requires:
    # of edges = # of nodes - 1
    can visit all nodes start from 1 node
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
        
        queue = deque([0])
        visited = set([0])
        while queue:
            node = queue.popleft()
            for neighbor in neighbors[node]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                
                
        return len(visited) == n
        
    def get_neighbors(self, edges):
        
        neighbors = defaultdict(list)
        
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
            
        return neighbors
