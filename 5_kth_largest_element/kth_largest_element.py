'''
=> Quick Select
Recursive
Time: O(n)
'''
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n <= 0:
            return -1
            
        return self.quick_select(nums, len(nums) - n, 0, len(nums) - 1)
    
    def quick_select(self, nums, k, start, end):
        if start >= end:
            return nums[start]
        
        # k represent index
        mid = start + (end - start) // 2
        pivot = nums[mid]
        l, r = start, end
        
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        if l <= k:
            return self.quick_select(nums, k, l, end)
        elif r >= k:
            return self.quick_select(nums, k, start, r)
        else:
            return nums[k]

'''
=> Quick Select
Non Recursive
Time: O(n)
'''        
class Solution2:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        return self.quick_select(nums, len(nums) - n, 0, len(nums) - 1)
        
    def quick_select(self, nums, k, start, end):
        while True:
            if start >= end:
                return nums[start]
                
            mid = start + (end - start) // 2
            pivot = nums[mid]
            
            l, r = start, end
            while l <= r:
                while l <= r and nums[l] < pivot:
                    l += 1
                while l <= r and nums[r] > pivot:
                    r -= 1
                
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                    
         
            if l <= k:
                start = l
            elif r >= k:
                end = r
            else:
                return nums[k]