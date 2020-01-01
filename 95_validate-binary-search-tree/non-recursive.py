'''
=> Iterative Inorder Traversal
Time: O(logn)
Space: O(nlog)

'''
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if not root:
            return True
        
        '''
             4
          2     6
        1   3  5  7
        '''
        stack = []
        lastNode = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if lastNode and root.val <= lastNode.val:
                return False
            lastNode = root
            root = root.right
        
        return True
            
        
