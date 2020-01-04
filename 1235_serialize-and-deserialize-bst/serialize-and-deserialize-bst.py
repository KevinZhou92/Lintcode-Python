"""
=> BFS
"""
from collections import deque
class Solution:
    def serialize(self, root):
        if not root:
            return '#'
            
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')
            
        return ','.join(res)

    def deserialize(self, data):
        if data == '#':
            return None
        
        data = data.split(',')    
        root = TreeNode(data[0])
        index = 1
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if data[index] == '#':
                node.left = None
            else:
                left = TreeNode(int(data[index]))
                node.left = left
                queue.append(left)
            index += 1
            if data[index] == '#':
                node.right = None
            else:
                right = TreeNode(int(data[index]))
                node.right = right
                queue.append(right)
            index += 1
            
        return root
                
            
                