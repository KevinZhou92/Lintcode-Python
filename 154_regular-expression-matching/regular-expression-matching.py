'''
s, p both char, compare and proceed to s+1, p+1

p '.|char *', match 0, 1, 2...and 
ab
.*
if cur is '.', 
    if next is '*', match s, p + 2
    if s[cur] == s[next], s + 1, p                    
p 'char*'  match 0, 1, 2, 




'''

class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        self.res_map = {}
        return self.dfs(s, p, 0, 0)
        
        
    def dfs(self, s, p, s_start, p_start):
        if (s_start, p_start) in self.res_map:
            return self.res_map[(s_start, p_start)]
        
        if p_start >= len(p):
            return s_start == len(s)
            
        if s_start >= len(s):
            return self.is_empty(p, p_start)
            
        res = False
        # a*
        # aa
        if p_start < len(p) - 1 and p[p_start + 1] == '*':
            res = (p[p_start] == '.' or p[p_start] == s[s_start]) and self.dfs(s, p, s_start + 1, p_start) or self.dfs(s, p, s_start, p_start + 2)
        else:
            res = (p[p_start] == '.' or p[p_start] == s[s_start]) and self.dfs(s, p, s_start + 1, p_start + 1)
        
        self.res_map[(s_start, p_start)] = res
        
        return res
        
    def is_empty(self, p, start):
        for i in range(start, len(p), 2):
            if i + 1 >= len(p) or p[i + 1] != '*':
                return False
        
        return True