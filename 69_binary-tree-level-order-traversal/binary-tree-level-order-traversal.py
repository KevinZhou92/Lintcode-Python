'''
=> Divide and Conquer
Time: O(logn) worst O(n)
Space: O(logn)
'''
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        
        level_map = {}
        self.traverse(root, 0, level_map)
        
        res = []
        for level in sorted(level_map.keys()):
            level_nodes = []
            for node in level_map[level]:
                level_nodes.append(node.val)
            res.append(level_nodes)
            
        return res
    
    def traverse(self, root, depth, level_map):
        if not root:
            return
        
        if depth not in level_map:
            level_map[depth] = []
            
        level_map[depth].append(root)
        self.traverse(root.left, depth + 1, level_map)
        self.traverse(root.right, depth + 1, level_map)