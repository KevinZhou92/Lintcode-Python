'''
=> Recursion
'''
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.res = []
        self.inorder(root)
        
        return self.res
    
    def inorder(self, root):
        if not root:
            return 
        
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

'''
=> Non-recursive
'''
class Solution2:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        res = []
        
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
            
        return res