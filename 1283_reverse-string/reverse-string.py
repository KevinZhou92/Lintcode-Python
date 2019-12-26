class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        if not s :
            return ""
            
        s = list(s.strip())
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        return ''.join(s)