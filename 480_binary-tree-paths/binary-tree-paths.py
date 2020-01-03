'''
=> Divide and Conquer
Time: O(n)
Space: O(n)
'''
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        
        if not root.left and not root.right:
            return [str(root.val)]
            
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        
        res = []
        for path in left_paths:
            res.append(str(root.val) + '->' + path)
        
        for path in right_paths:
            res.append(str(root.val) + '->' + path)
            
        return res
            
