'''
Remember to backtrack!!!!!
'''
import copy
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
            
        res = []
        self.dfs(root, target, [], res)
        
        return res
        
    def dfs(self, root, target, path, res):
        if not root:
            return
    
        if not root.left and not root.right:
            target -= root.val
            path.append(root.val)
            if target == 0:
                res.append(copy.copy(path))
            path.pop()
            
            return
        
        path.append(root.val)
        target -= root.val
        self.dfs(root.left, target, path, res)
        self.dfs(root.right, target, path, res)
        path.pop()