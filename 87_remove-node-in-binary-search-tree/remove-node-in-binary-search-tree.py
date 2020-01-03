'''
=> Divide and Conquer
Time: O(logn)
Space: O(n)

!!! Revisit!
'''
from util_class import TreeNode
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return
        
        dummy = TreeNode(0)
        dummy.left = root
        target_node, parent = self.find_node(root, dummy, value)
        if not target_node:
            return root
            
        self.remove_node(target_node, parent)
        
        return dummy.left
        
    # find parent of a node
    def find_node(self, node, parent, value):
        if not node:
            return None, None
            
        if node.val < value:
            return self.find_node(node.right, node, value)
        elif node.val > value:
            return self.find_node(node.left, node, value)
        elif node.val == value:
            return node, parent
        

    def remove_node(self, node, parent):
        if not node.left and not node.right:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return
        
        if not node.left or not node.right:
            if parent.left == node:
                parent.left = node.left if node.left else node.right
                return
            else:
                parent.right = node.left if node.left else node.right
                return
                
        father = node
        left_max = node.left
        while left_max.right:
            father = left_max
            left_max = left_max.right

        if father.left == left_max:
            father.left = None
        elif father.right == left_max:
            father.right = None
            
        
        if parent.left == node:
            parent.left = left_max
            left_max.left = node.left
            left_max.right = node.right
        else:
            parent.right = left_max 
            left_max.left = node.left
            left_max.right = node.right
        
        node.left = None
        node.right = None
            
            