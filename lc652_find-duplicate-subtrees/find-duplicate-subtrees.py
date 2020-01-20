'''
=> Post-order traversal

Time: o(n)
Space: O
'''
from util_class import TreeNode
from collections import defaultdict
from typing import List
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        paths = defaultdict(int)
        
        self.post_order(root, paths, res)
        
        return res
    
    def post_order(self, root, paths, res):
        if not root:
            return '*'
        
        serialization = self.post_order(root.left, paths, res) + self.post_order(root.right, paths, res) + str(root.val)
        paths[serialization] += 1
        if paths[serialization] == 2:
            res.append(root)
            
        return serialization
        