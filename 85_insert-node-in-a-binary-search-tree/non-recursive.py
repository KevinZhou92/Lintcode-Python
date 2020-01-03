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
            
        cur_node = root
        while cur_node:
            if cur_node.val < node.val:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = node
                    cur_node = None
            else:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = node
                    cur_node = None
                    
                    
        return root