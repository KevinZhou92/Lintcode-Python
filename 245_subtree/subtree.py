'''
=> DFS
Time: O(n)
Space: O(n)
Note:
    check if subtree, we need to check:
    1. If it is subtree from current T1's node, root of T2
    2. If #1 doesn't satisfy, we will check T1's left with root of T2 and T1's right with root of T2
'''
class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        if not T1 and not T2:
            return True
            
        if not T1:
            return False
        
        if not T2:
            return True
            
        if self.is_equal(T1, T2):
            return True
            
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        
        
    def is_equal(self, T1, T2): 
        # if not T2 or not T1:
        #    return T1 == T2
        if not T2 and not T1:
            return True
        
        if not T1 or not T2:
            return False
            
        if T1.val != T2.val:
            return False
        
        return self.is_equal(T1.left, T2.left) and self.is_equal(T1.right, T2.right)
        
      