"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        
        stack1 = [root]
        normal_order = False
        res = []
        level_nodes = []
        while stack1:
            stack2 = []
            size = len(stack1)
            for i in range(size):
                cur_root = stack1.pop()
                level_nodes.append(cur_root.val)
                if normal_order:
                    if cur_root.right:
                        stack2.append(cur_root.right)
                    if cur_root.left:
                        stack2.append(cur_root.left)
                else:
                    if cur_root.left:
                        stack2.append(cur_root.left)
                    if cur_root.right:
                        stack2.append(cur_root.right)
            res.append(level_nodes)
            level_nodes = []
            normal_order = not normal_order
            stack1 = stack2
        
        return res
                