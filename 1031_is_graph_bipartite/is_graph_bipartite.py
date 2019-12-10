'''
In the mathematical field of graph theory, a bipartite graph (or bigraph) is a graph whose vertices can be divided into two disjoint and independent sets U and V such that every edge connects a vertex in U to one in V. Each edge won't connect tow vertices in the same set. So the color at two ends must be different.
'''


'''
=> BFS
for each vertice, if not colored, color it with red(1)
    check vertice's neighbour, if not colored, color with blue(-1), put in queue
    if already colored, the color shoul not be the same as vertice itself
In BFS method, we progressively colored all vertices and make sure they are not painted in the same way
'''

class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """

    def isBipartite(self, graph):
        # Write your code here
        from collections import deque 
        
        deque = deque([])
        colors = [0] * len(graph)
        
        for i in range(len(graph)):
            if colors[i] != 0:
                continue
            colors[i] = 1
            deque.append(i)
            while deque:
                node = deque.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        deque.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
                    
        return True

'''
=> DFS
# time : O(V + E)
# space: O(V)
# topic: dfs, graph

Thought: If current vertice is not colored, give it a color and search on it neighbour, execute 
dfs on neighbour node, make sure we switch color when color the neighbour node. During dfs, if we find 
the current vertice is colored, we check if it is the required color, it not, return false
'''
class Solution2:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here
        colors = [0] * len(graph)
        
        for index in range(len(graph)):
            if colors[index] == 0 and not self.dfs(graph, colors, index, 1):
                return False
                
        return True
    
    def dfs(self, graph, colors, index, color):
        if colors[index] == color:
            return True
            
        colors[index] = color
        for neighbour in graph[index]:
            if colors[neighbour] != 0 and colors[neighbour] != -color:
                return False
            if not self.dfs(graph, colors, neighbour, -color):
                return False
            
        return True