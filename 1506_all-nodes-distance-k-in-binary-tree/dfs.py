'''
=> DFS

Time: O(n)
Space: O(n)
'''`
from util_class import TreeNode
class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    """
    def distanceK(self, root, target, K):
        # Write your code here
        if K == 0:
            return [target.val]
        
        res = []
        self.dfs(root, target, K, res)
        
        return res
        
    # return distance of target to this node
    def dfs(self, root, target, K, res):
        if not root:
            return -1
        
        if root == target:
            self.collect(root, K, res)
            return 1
            
        left = self.dfs(root.left, target, K, res)
        right = self.dfs(root.right, target, K, res)
        if left >= 0:
            if left == K: 
                res.append(root.val)
            self.collect(root.right, K - left - 1, res)
            return left + 1
        elif right >= 0:
            if right == K:
                res.append(root.val)
            self.collect(root.left, K - right - 1, res)
            return right + 1
        
        return -1
    
    def collect(self, root, dis, res):
        if not root or dis < 0:
            return 
        if dis == 0:
            res.append(root.val)
        self.collect(root.left, dis - 1, res)
        self.collect(root.right, dis - 1, res)
            
        