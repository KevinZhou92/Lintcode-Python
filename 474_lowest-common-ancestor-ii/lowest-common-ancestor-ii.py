"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        if root == A or root == B:
            return root
            
        A_parent, B_parent = A, B
        visited = set()
        while A_parent:
            visited.add(A_parent)
            A_parent = A_parent.parent
            
        while B_parent:
            if B_parent not in visited:
                B_parent = B_parent.parent
            else:
                return B_parent
                
        return None
