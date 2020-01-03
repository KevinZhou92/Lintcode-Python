"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        if not root:
            return 0
            
        return self.helper(root)[0]
    
    # subtree_max, increasing_len(top to bottom), decreasing_len(top to bottom)    
    def helper(self, root):
        if not root:
            return 0, 0, 0
            
        left_max, left_increasing, left_decreasing = self.helper(root.left)
        right_max, right_increasing, right_decreasing = self.helper(root.right)
        
        res = [1, 1, 1]
        res[0] = max(res[0], left_max, right_max)
        
        #0 global max
        #1 bottom to top increasing
        #2 bottom to top decreasing
    
        if root.left:
            # left decrease to right
            if root.val + 1 == root.left.val:
                res[2] = max(res[2], left_decreasing + 1)
            
            if root.val - 1 == root.left.val:
                res[1] = max(res[1], left_increasing + 1)
                
            res[0] = max(res[0], left_max, right_max, res[1], res[2])
            
        if root.right:
            if root.val + 1 == root.right.val:
                res[2] = max(res[2], right_decreasing + 1)
                res[0] = max(res[0], res[1] + res[2] - 1)
            
            if root.val - 1 == root.right.val:
                res[1] = max(res[1], right_increasing + 1)
                res[0] = max(res[0], res[1] + res[2] - 1)
            
            res[0] = max(res[0], left_max, right_max, res[1], res[2])
            
        return res
                
        