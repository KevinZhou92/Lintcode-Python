'''
=> Divide and Conquer
'''
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        
        return self.helper(root)[0]
       
    # child_max, cur_len 
    #
    def helper(self, root):
        if not root:
            return 0, 0
            
        left_max, left_len = self.helper(root.left)
        right_max, right_len = self.helper(root.right)
        
        res = [1, 1]
        
        if root.left and root.val + 1 == root.left.val:
            res[1] = max(res[1], left_len + 1)
        if root.right and root.val + 1 == root.right.val:
            res[1] = max(res[1], right_len + 1)
        res[0] = max(res[1], left_max, right_max)
         
        return res
        
        
        
        