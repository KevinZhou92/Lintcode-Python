'''
Time: O(n)
Space: O(1)
'''
class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        if not root:
            return None
    
        index_A = self.get_height(root, A)
        index_B = self.get_height(root, B)
        
        while index_A > 0 and index_B > 0:
            if index_A > index_B:
                A = A.parent
                index_A -= 1
            elif index_B > index_A:
                B = B.parent
                index_B -= 1
            else:
                if A == B:
                    return A
                A = A.parent
                index_A -= 1
                B = B.parent
                index_B -= 1
                
        return None
        
    def get_height(self, root, node):
        count = 0
        
        while node:
            node = node.parent
            count += 1
            
        return count
            