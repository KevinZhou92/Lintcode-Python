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
        
        root = node
        nodes = self.get_nodes(node)
        
        node_map = {}
        for node in nodes:
            node_map[node] = UndirectedGraphNode(node.label)
            
        for node in nodes:
            for neighbor in node.neighbors:
                node_map[node].neighbors.append(node_map[neighbor])
                
        return root
        
    def get_nodes(self, node):
        queue = deque([node])
        nodes = set([node])
        
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    queue.append(neighbor)
                    nodes.add(neighbor)
                
        return nodes