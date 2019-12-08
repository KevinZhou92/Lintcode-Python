'''
=> Bucket Sort
[1, 9, 2, 5]
put number into bucket 
reserve max and min number in bucket 
if gap is evenly distributed, then this is the min gap, min_gap = (max - min) // (n - 1)
bucket_count = (max - min) // min_gap
max_bucket - keep track of min number in bucket
min_bucket - keep track of max number in bucket

max - min

'''
class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here

        if len(nums) == 2:
            return abs(nums[0] - nums[1])
            
        max_num = max(nums)
        min_num = min(nums)
        
        # corner case
        if max_num == min_num:
            return 0
        
        bucket_size = (max_num - min_num) // (len(nums) - 1) + 1
        bucket_count = (max_num - min_num) // bucket_size + 1
        
        max_bucket = [-sys.maxsize for i in range(bucket_count)]
        min_bucket = [sys.maxsize for i in range(bucket_count)]
        
        for num in nums:
            bucket_id = (num - min_num) // bucket_size
            min_bucket[bucket_id] = min(min_bucket[bucket_id], num)
            max_bucket[bucket_id] = max(max_bucket[bucket_id], num)
            
        res = -sys.maxsize
        min_value = max_bucket[0]
        for i in range(1, bucket_count):
            if min_bucket[i] == sys.maxsize:
                continue
            res = max(res, min_bucket[i] - min_value)
            min_value = max_bucket[i]
        
        return res