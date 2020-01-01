'''
=> Divide and Conquer
Time: O(logn)
Space: O(n)

Note:
1. Check left and right subtrees are valid bsts. Return the min, max value in subtrees
2. If both left and right are valid, check current root:
we need to make sure left_max < root.val < right min, and both left and right are valid subtrees.
Then we know, current bst is a valid one.
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
        
        is_valid, _, _ = self.traverse(root)
        
        return is_valid
        
    def traverse(self, root):
        if not root:
            return True, sys.maxsize, -sys.maxsize - 1
            
        left_is_valid, left_min, left_max = self.traverse(root.left)
        right_is_valid, right_min, right_max = self.traverse(root.right)
        
        if left_is_valid and right_is_valid and left_max < root.val < right_min:
            return True, min(left_min, root.val, right_min), max(left_max, right_max, root.val)
        
        return False, None, None