'''
=> Recursion
'''
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    res = []
    def preorderTraversal(self, root):
        # write your code here
        self.res = []
        self.preorder(root)
        
        return self.res
        
    def preorder(self, root):
        if not root:
            return
        
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

class Solution2:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

'''
=> Non-recursive
For non recursive solution, we need to simulate the stack operation, we should refer to the recursive solution and implement non-recursive solution by using stack. For example,  
'root' represent the root node in current stack frame, once we arrive at the left most child node, we will check the left child by assigning it to 'root' variable, it is like pushing another frame to the stack, then we return from the None(since its left node is none) and pop the node out, check its right child. We will follow this manner on other part of the tree.
'''
class Solution3:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    res = []
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        stack = []
        res = []
        
        while root or stack:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
                
            root = stack.pop().right
        
        return res