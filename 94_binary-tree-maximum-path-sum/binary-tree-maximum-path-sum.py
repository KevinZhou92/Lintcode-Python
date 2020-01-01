'''
=> Divide Conquer
Time: O(n)
Space:  O(n)

Note: Always divide & conquer
In this question, we need to find:
1. Max path sum from left and right subtree, left_max, right_max
2. Max path sum including current root, could be [left_sum + root.val, right_sum + root.val, root.val]
Don't ignore the last case, the max sum could be root it self.
3. Get global max path sum from left_max and right_max and path sum max, return global max and cur path max to upper level
'''

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        if not root:
            return 0
        res = self.get_sum(root)
        print(res)
        return res[0]
        
    
    # left max sum, left path sum 
    # right max_sum, right path_sum
    #     5
    #  -3    6
    #-4  1  7  8
    #
    def get_sum(self, root):
        if not root:
            return -sys.maxsize, 0
            
        left_max, left_sum = self.get_sum(root.left)
        right_max, right_sum = self.get_sum(root.right)
        
        path_max = max(max(left_sum, right_sum) + root.val, root.val)
        cur_max = max(left_max, right_max, root.val + left_sum + right_sum, path_max)
        
        return cur_max, path_max
        