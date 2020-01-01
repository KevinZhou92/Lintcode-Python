'''
=> DFS
Time: O(N)
'''
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.res = sys.maxsize
        self.node = None
        self.get_sum(root)
        
        return self.node
        
    def get_sum(self, root):
        if not root:
            return 0
            
        left_sum = self.get_sum(root.left)
        right_sum = self.get_sum(root.right)
        if self.res > left_sum + right_sum + root.val:
            self.res = left_sum + right_sum + root.val
            self.node = root
        
        return root.val + left_sum + right_sum