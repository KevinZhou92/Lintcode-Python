class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # write your code here
        if not a or not b:
            return a == b
            
        return a.val == b.val and self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right) 
        
        
