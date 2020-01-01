'''
=> DFS
Time: O(n)
Space: O(n)
'''
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        
        return self.dfs(root)
        
    def dfs(self, root):
        if not root:
            return 0
            
        if not root.left and not root.right:
            return 1
            
        res = sys.maxsize
        if root.left:
            res = min(res, self.dfs(root.left))
        
        if root.right:
            res = min(res, self.dfs(root.right))
        
        return res + 1


class Solution2:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        
        return self.dfs(root)
        
    def dfs(self, root):
        if not root:
            return sys.maxsize
            
        if not root.left and not root.right:
            return 1
            
        return min(self.dfs(root.left), self.dfs(root.right)) + 1
