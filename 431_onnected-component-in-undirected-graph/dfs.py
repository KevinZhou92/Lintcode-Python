'''
=> DFS

Time: O(n)
Space: O(n)
'''
class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        if not nodes:
            return []
            
        res = []
        visited = set()
        for node in nodes:
            if node in visited: 
                continue
            path = []
            self.dfs(node, visited, path)
            res.append(sorted(path))
            
        return res
        
    def dfs(self, node, visited, path):
        if node in visited:
            return
        
        path.append(node.label)
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited, path, res)
        