'''
=> KMP
Time: O(n)
Space: O(m)
'''
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if not target:
            return 0
            
        if not source:
            return -1
        
        lps = self.get_lps(target)
        
        l,r = 0, 0
        while l < len(source):
            if target[r] == source[l]:
                l += 1
                r += 1
                if r == len(target):
                    return l - r
            elif r > 0:
                r = lps[r - 1]
            else:
                l += 1
                
        return -1
        
    def get_lps(self, string):
        lps = [0 for i in range(len(string))]
        # aacaa
        l , r = 0, 1
        
        while r < len(string):
            if string[l] == string[r]:
                l += 1
                lps[r] = l
                r += 1
            elif l > 0:
                l = lps[l - 1]
            else:
                r += 1
                
        return lps