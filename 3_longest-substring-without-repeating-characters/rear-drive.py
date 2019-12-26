'''
=> Two Pointer
Drive by left pointer
'''
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        r, res, chars = 0, 0, set()
        for l in range(len(s)):
            while r < len(s) and s[r] not in chars:
                chars.add(s[r])
                r += 1
            res = max(res, len(chars))
            chars.remove(s[l])
            
        return res