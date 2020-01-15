from collections import defaultdict, deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
            
        # build inverse relationships
        inverse_edges = defaultdict(set)
        for prerequisite in prerequisites:
            inverse_edges[prerequisite[0]].add(prerequisite[1])
            
        # 1 visiting        
        # 0 unvisited
        # -1 visited
        visited = [0 for i in range(numCourses)]
        res = []
        for node in range(numCourses):
            if self.dfs(node, inverse_edges, visited, res):
                return []
                
        return res
        
    # True for circle
    # False for no circle
    def dfs(self, node, inverse_edges, visited, res):
        if visited[node] == 1:
            return True
        if visited[node] == -1:
            return False
            
        visited[node] = 1
        for pre_node in inverse_edges[node]:
            if self.dfs(pre_node, inverse_edges, visited, res):
                return True
            
        visited[node] = -1
        res.append(node)
        
        return False
        
