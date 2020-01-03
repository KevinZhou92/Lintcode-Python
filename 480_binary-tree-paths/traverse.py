class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        res = []
        self.traverse(root, '', res)
        
        return res
    
    def traverse(self, root, path, res):
        if not root.left and not root.right:
            res.append(path + str(root.val))
            return
        
        path = path + str(root.val) + '->'
        if root.left:
            self.traverse(root.left, path, res)
        if root.right:
            self.traverse(root.right, path, res)