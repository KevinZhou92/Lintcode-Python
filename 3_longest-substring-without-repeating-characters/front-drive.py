'''
=> Two Pointer
Drive by right pointer
'''
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        l, res, indices = 0, 0, {}
        for r in range(len(s)):
            if s[r] in indices:
                l = max(l, indices[s[r]] + 1)
            res = max(res, r - l + 1)
            indices[s[r]] = r
            
        return res

class Solution2:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        l, res, chars = 0, 0, set()
        for r in range(len(s)):
            while l < r and s[r] in chars:
                chars.discard(s[l])
                l += 1
            res = max(res, r - l + 1)
            chars.add(s[r])
            
        return res