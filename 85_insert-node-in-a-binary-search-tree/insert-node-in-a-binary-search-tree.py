class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        
        self.insert(root, node)
        
        return root
        
    def insert(self, root, node):
        
        if root.val > node.val:
            if root.left:
                self.insert(root.left, node)
            else:
                root.left = node
                return
        elif root.val < node.val:
            if root.right:
                self.insert(root.right, node)
            else:
                root.right = node
                return    


class Solution2:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
            
        return root
        