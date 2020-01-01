'''
=> Inorder Traversal

Note: Inorder traversal for BST are always in ascending order.
'''
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        inorder_traversal = self.inorder_traversal(root)
        
        for i in range(0, len(inorder_traversal) - 1):
            if inorder_traversal[i] >= inorder_traversal[i + 1]:
                return False
        
        return True
        
    def inorder_traversal(self, root):
        if not root:
            return []
            
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)
        