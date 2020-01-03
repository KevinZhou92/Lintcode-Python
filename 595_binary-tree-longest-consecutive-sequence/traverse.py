'''
=> Traverse
Time: O(logn) worst O(n)
Space: O(n)
'''
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        if not root:
            return 0
        
        self.res = -sys.maxsize - 1
        self.helper(root, 1)
        
        return self.res
        
    def helper(self, root, seq_len):
        self.res = max(self.res, seq_len)
        if not root:
            return
        
        if root.left:
            if root.left.val - 1 == root.val:
                self.helper(root.left, seq_len + 1)
            else:
                self.helper(root.left, 1)
                
        if root.right:
            if root.right.val - 1 == root.val:
                self.helper(root.right, seq_len + 1)
            else:
                self.helper(root.right, 1)
        
        
