"""
=> DFS(Preorder traversal)
Use deque to optimize deserialization.
"""
from collections import deque
from util_class import TreeNode
class Solution:
    def serialize(self, root):
        
        def dfs(root):
            if not root:
                return ['#']
            return [str(root.val)] + dfs(root.left) + dfs(root.right)
            
        return ','.join(dfs(root))

    def deserialize(self, data):
        if data == '#':
            return None
            
        data = deque(data.split(','))
        def dfs(data):
            if not data:
                return None
                
            if  data[0] == '#':
                data.popleft()
                return None
            
            root = TreeNode(int(data.popleft()))
            root.left = dfs(data)
            root.right = dfs(data)
            
            return root
        
        return dfs(data)
            
            