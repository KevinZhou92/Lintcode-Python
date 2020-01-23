"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        if not nodes:
            return []
            
        
        visited = set()
        res = []
        for node in nodes:
            if node not in visited:
                path = []
                component_visited = set()
                path.append(node.label)
                queue = deque([node])
                visited.add(node)
                component_visited.add(node)
                while queue:
                    cur = queue.popleft()
                    for neighbor in cur.neighbors:
                        if neighbor not in component_visited:
                            component_visited.add(neighbor)
                            visited.add(neighbor)
                            path.append(neighbor.label)
                            queue.append(neighbor)
                res.append(sorted(path))
                
        return res
            
        