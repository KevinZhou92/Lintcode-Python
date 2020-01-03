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
            
        return self.helper(root, target)
        
    def helper(self, root, target):
        res = []
        if not root:
            return []
        
        if not root.left and not root.right and root.val == target:
            return [[root.val]]
            
        left = self.helper(root.left, target - root.val)
        right = self.helper(root.right, target - root.val)
        
        for left_res in left:
            tmp = [root.val] + left_res
            res.append(tmp)
        
        for right_res in right:
            tmp = [root.val] + right_res
            res.append(tmp)
            
        return res
