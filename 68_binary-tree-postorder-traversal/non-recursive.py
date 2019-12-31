'''
=> Non-recursive
In non-recursive postorder traversal, we should not directly pop the current root node, because after iterating the right subtree, we still 
'''  
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        res = []
        
        last = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1].right
            if not root or root == last:
                root = stack.pop()
                res.append(root.val)
                last = root
                root = None
        
        return res
                