from collections import deque
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None
            
        node_map = {}
        visited = set([node])
        
        queue = deque([node])
        while queue:
            orig_node = queue.popleft() 
            if orig_node not in node_map:
                new_node = UndirectedGraphNode(node.label)
                node_map[orig_node] = new_node
            else:
                new_node = node_map[orig_node]
            for neighbor in orig_node.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = UndirectedGraphNode(neighbor.label)
                new_node.neighbors.append(node_map[neighbor])    
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        return node
            
        
        
