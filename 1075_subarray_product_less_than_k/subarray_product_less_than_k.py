'''
=> Prefix Product
O(n^2)
[10, 5, 2, 6] 110
 10  50 100 600

'''
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the number of subarrays where the product of all the elements in the subarray is less than k
    """
    def numSubarrayProductLessThanK(self, nums, k):
        # Write your code here
        if not nums or k <= 0:
            return 0
        
        res = 0
        product = 1
        left = 0
        right = 0
        
        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            res += right - left + 1
            right += 1
            
        return res

# Time: O(n)
# Space: O(1)