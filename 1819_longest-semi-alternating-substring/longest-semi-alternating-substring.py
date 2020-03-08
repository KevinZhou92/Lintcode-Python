'''
=> Sliding Window
'''
class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        # write your code here
        if len(s) < 3:
            return len(s)
            
        cnt, l, first, res = 1, 0, 0, 1
        for index in range(1, len(s)):
            if s[index - 1] == s[index]:
                cnt += 1
            else:
                cnt = 1
                first = index
                
            if cnt == 3:
                cnt -= 1
                first += 1
                l = first + 1
                
            res = max(res, index - l + 1)
            
        return res 