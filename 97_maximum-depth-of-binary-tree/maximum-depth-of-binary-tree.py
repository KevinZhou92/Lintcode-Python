
'''
=> Bottom-up DFS
Time: O(logn) worst O(n)
Space: O(n)
'''
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        return max(left, right) + 1  

'''
=> Top-Down DFS
Time: O(n)
Space: O(n)
'''
class Solution2:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        self.res = 0
        self.dfs(root, 0)
        
        return self.res
        
    def dfs(self, root, depth):
        if not root:
            self.res = max(self.res, depth)
            return 
        
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
        