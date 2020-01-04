'''
=> BFS
'''
from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return '#'
            
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append('#')
                
        return ','.join(res)
    
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data == '#':
            return None
            
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if index >= len(data) or data[index] == '#':
                node.left = None
            else:
                left = TreeNode(int(data[index]))
                queue.append(left)
                node.left = left
            index += 1
            if index >= len(data) or data[index] == '#':
                node.right = None
            else:
                right = TreeNode(int(data[index]))
                queue.append(right)
                node.right = right
            index += 1
            
        return root
        
