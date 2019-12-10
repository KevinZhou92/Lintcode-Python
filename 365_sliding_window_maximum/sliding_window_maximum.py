'''
=> Sliding window
!!! Remember, we don't need to always store value in data structure, 
we can store index or prefix to achieve some goal.
[1,2,7,7,8]
k = 3

keep track of the biggest, 2nd biggest number... in queue
for every number, check if biggest is out of queue, find the next biggest and add to result
'''
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        from collections import deque
        
        if k == 0 or len(nums) < k:
            return []
            
        res = []
        deque = deque([])
        
        for i in range(k):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
                
        for i in range(k, len(nums)):
            res.append(nums[deque[0]])
            if i - deque[0] == k: 
                deque.popleft()
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
        res.append(nums[deque[0]])    
        
        return res