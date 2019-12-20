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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        res = []
        if not root:
            return res
            
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

'''
=> Non-recursive
'''        
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution2:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    # self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    def postorderTraversal(self, root):
        # write your code here
        res = []
        stack = []
        
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1].right
            if not root or prev == root:
                prev = stack.pop()
                res.append(prev.val)
                root = None
            
        return res