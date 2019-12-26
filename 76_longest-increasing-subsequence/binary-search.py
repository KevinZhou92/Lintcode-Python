'''
=> Binary Search
Time: O(nlogn)
Space: O(n)
Reference: https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/300-zui-chang-shang-sheng-zi-xu-lie-by-alexer-660/
'''
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        tails = []
        
        for index, num in enumerate(nums):
            index = self.find(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
                
        return len(tails)
        
    def find(self, tails, num):
        if not tails:
            return 0
            
        start, end = 0, len(tails) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if tails[mid] >= num:
                end = mid
            else:
                start = mid
                
        if tails[start] >= num:
            return start
            
        if tails[end] >= num:
            return end
    
        return len(tails)
                
        