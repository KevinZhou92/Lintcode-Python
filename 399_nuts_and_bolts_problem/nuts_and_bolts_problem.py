"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        self.qsort(nuts, bolts, 0, len(nuts) - 1, compare)
        
        return 
    
    def qsort(self, nuts, bolts, start, end, compare):
        if start >= end:
            return 
        
        index = self.partition(nuts, start, end, compare, bolts[start])
        self.partition(bolts, start, end, compare, nuts[index])
        self.qsort(nuts, bolts, start, index - 1, compare)
        self.qsort(nuts, bolts, index + 1, end, compare)
        
    def partition(self, nums, start, end, compare, pivot):
        pivot_index = -1
        for index, num in enumerate(nums):
            if self.cmp(num, pivot, compare) == 0:
                pivot_index = index
                break
        
        nums[start], nums[pivot_index] = nums[pivot_index], nums[start]
        l, r = start + 1, end
        while l <= r:
            while l <= r and self.cmp(nums[l], pivot, compare) < 0:
                l += 1
            
            while l <= r and self.cmp(nums[r], pivot, compare) > 0:
                r -= 1
                
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        nums[r], nums[start] = nums[start], nums[r]
        
        return r
        
    def cmp(self, a, b, compare):
        return -compare.cmp(b, a) if compare.cmp(a, b) == 2 else compare.cmp(a, b)