'''
Inorder Traversal
'''
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        if not self.hasNext():
            return None
            
        root = self.stack.pop()
        cur = root.right
        
        while cur:
            self.stack.append(cur)
            cur = cur.left
            
        return root