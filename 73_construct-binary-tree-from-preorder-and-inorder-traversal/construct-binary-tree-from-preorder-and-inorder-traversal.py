'''
=> Divide and Conquer
Time: O(logn) worst O(n)
Space: O(n)
'''
from util_class.TreeNode import TreeNode
class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder and not inorder:
            return None
            
        if len(preorder) != len(inorder):
            return None
            
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
    
    def build(self, preorder, p_start, p_end, inorder, in_start, in_end):
        #    1
        #  2    3
        #4  5  6  7    
        #pre 1245367
        #in  4251637
        if in_start > in_end or p_start > p_end:
            return None
        
        root = TreeNode(preorder[p_start])
        root_index = self.find_root_index(inorder, in_start, in_end, root.val)
        root.left = self.build(preorder, p_start + 1, p_start + root_index - in_start, inorder, in_start, root_index - 1)
        root.right = self.build(preorder, p_start + root_index - in_start + 1, p_end, inorder, root_index + 1, in_end)
        
        return root

    # In python, we could use list.index(element) to find the index of specific element(only if there are no duplicates)    
    def find_root_index(self, nums, start, end, target):
        for i in range(start, end + 1):
            if nums[i] == target:
                return i
                
        return -1
        
        