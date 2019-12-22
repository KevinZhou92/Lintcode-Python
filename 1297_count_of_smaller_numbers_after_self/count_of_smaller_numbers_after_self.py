'''
=> Merge Sort
Sort in reverse order
'''
class Num:
    def __init__(self, num, index):
        self.num = num
        self.index = index
        
class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def countSmaller(self, nums):
        # write your code here
        Nums = []
        
        for i in range(len(nums)):
            Nums.append(Num(nums[i], i))
            
        res = [0] * len(nums)
        self.merge_sort(Nums, 0, len(nums) - 1, res)
        
        return res
    
    def merge_sort(self, nums, start, end, res):
        if start >= end:
            return 
        
        mid = start + (end - start) // 2
        self.merge_sort(nums, start, mid, res)
        self.merge_sort(nums, mid + 1, end, res)
        self.merge(nums, start, mid, end, res)
        
    def merge(self, nums, start, mid, end, res):
        l, r = start, mid + 1
        tmp = [0] * (end - start + 1) 
        index = 0
        while l <= mid and r <= end:
            if nums[l].num > nums[r].num:
                tmp[index] = nums[l]
                num_index = nums[l].index
                res[num_index] += end - r + 1
                l += 1
            else:
                tmp[index] = nums[r]
                r += 1
            index += 1
            
        while l <= mid:
            tmp[index] = nums[l]
            l += 1
            index += 1
            
        while r <= end:
            tmp[index] = nums[r]
            r += 1
            index += 1
                
                
        for i in range(len(tmp)):
            nums[start + i] = tmp[i]


'''
=> Merge Sort
Sort in natural order
'''     
class Solutio2:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def countSmaller(self, nums):
        # write your code here
        Nums = []
        
        for i in range(len(nums)):
            Nums.append(Num(nums[i], i))
            
        res = [0] * len(nums)
        self.merge_sort(Nums, 0, len(nums) - 1, res)
        
        return res
    
    def merge_sort(self, nums, start, end, res):
        if start >= end:
            return 
        
        mid = start + (end - start) // 2
        self.merge_sort(nums, start, mid, res)
        self.merge_sort(nums, mid + 1, end, res)
        self.merge(nums, start, mid, end, res)
        
    def merge(self, nums, start, mid, end, res):
        l, r = start, mid + 1
        tmp = [0] * (end - start + 1) 
        index = 0
        smaller_count = 0
        while l <= mid and r <= end:
            if nums[l].num > nums[r].num:
                tmp[index] = nums[r]
                smaller_count += 1
                r += 1
            else:
                num_index = nums[l].index
                res[num_index] += smaller_count
                tmp[index] = nums[l]
                l += 1
            index += 1
            
        while l <= mid:
            num_index = nums[l].index
            res[num_index] += end - mid
            tmp[index] = nums[l]
            l += 1
            index += 1
            
        while r <= end:
            tmp[index] = nums[r]
            r += 1
            index += 1
                
                
        for i in range(len(tmp)):
            nums[start + i] = tmp[i]