'''
=> Divide and Conquer

Note:
Be clear about what needs to be returned to bigger problem
Be clear about the subproblems
'''
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
        
        if not root.left and not root.right:
            if target == root.val:
                return [[root.val]]
            return []
            
        left_paths = self.binaryTreePathSum(root.left, target - root.val)
        right_paths = self.binaryTreePathSum(root.right, target - root.val)
        
        res = []
        for left_path in left_paths:
            res.append([root.val] + left_path)
        
        for right_path in right_paths:
            res.append([root.val] + right_path)
            
        return res