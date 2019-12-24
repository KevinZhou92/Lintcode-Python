'''
=> BFS
'''
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegree = {}
        
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor.label] = indegree.get(neighbor.label, 0) + 1
       
        res = []
        d = deque([])
        for node in graph:
            if node.label not in indegree:
                d.append(node)
    
        while d:
            node = d.popleft()
            res.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor.label] -= 1
                if indegree[neighbor.label] == 0:
                    d.append(neighbor)
                    
        return res
        
'''
=> DFS
'''
class Solution2:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegree = {}
        
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor.label] = indegree.get(neighbor.label, 0) + 1
                
        res = []
        for node in graph:
            if node.label not in indegree:
                self.dfs(indegree, node, res)
                
        return res
        
    def dfs(self, indegree, node, res):
        res.append(node)
        
        for neighbor in node.neighbors:
            indegree[neighbor.label] -= 1
            if indegree[neighbor.label] == 0:
                self.dfs(indegree, neighbor, res)
        