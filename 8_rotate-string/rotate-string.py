'''
=> Three Steps Flip
Time: O(n)
'''
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        # abcde 3  cdeab
        if offset == 0:
            return s
        if not s:
            return ""
        # abcdefg  dcbagfe 
        self.reverse(s, 0, len(s) - 1)
        self.reverse(s, 0, offset % len(s) - 1)
        self.reverse(s,  offset % len(s), len(s) - 1)
        
        return s
        
    def reverse(self, s, start, end):
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            
            