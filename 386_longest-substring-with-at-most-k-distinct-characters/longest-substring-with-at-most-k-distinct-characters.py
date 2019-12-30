'''
=> HashMap
Time: O(n)
'''
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s:
            return 0
        
        l = 0
        visited = {}
        res = 0
        for r in range(len(s)):
            visited[s[r]] = visited.get(s[r], 0) + 1
            while l <= r and len(visited) > k:
                visited[s[l]] = visited.get(s[l]) - 1
                if visited[s[l]] == 0:
                    visited.pop(s[l])
                l += 1
            res = max(res, r - l + 1)
            
        return res
                