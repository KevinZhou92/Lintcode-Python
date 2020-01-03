'''
=> Divide and Conquer
Note:
Maximum average
'''
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        if not root:
            return None
            
        return self.get_min_subtree(root)[0]
        
    def get_min_subtree(self, root):
        if not root:
            return None, 0, 0, 0, 0
            
        left_min_node, left_min_sum, left_min_count, left_sum, left_count = self.get_min_subtree(root.left)
        right_min_node, right_min_sum, right_min_count, right_sum, right_count = self.get_min_subtree(root.right)
        
        res = [root, root.val + left_sum + right_sum, 1 + left_count + right_count, root.val + left_sum + right_sum, 1 + left_count + right_count]
        
        if left_min_sum * res[2] > res[1] * left_min_count:
            res[0] = left_min_node
            res[1] = left_min_sum
            res[2] = left_min_count
        
        if right_min_sum * res[2] > right_min_count * res[1]:
            res[0] = right_min_node
            res[1] = right_min_sum
            res[2] = right_min_count
            
        return res