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
        self.traverse(root, target - root.val, [root.val], res)
        
        return res
        
    def traverse(self, root, target, path, res):
        # exit condition: leaf node
        if not root.left and not root.right:
            if target == 0:
                res.append(copy.copy(path))
            return
        
        if root.left:
            # backtrack
            path.append(root.left.val)
            self.traverse(root.left, target - root.left.val, path, res)
            path.pop()
            
        if root.right:
            path.append(root.right.val)
            self.traverse(root.right, target - root.right.val, path, res)
            path.pop()