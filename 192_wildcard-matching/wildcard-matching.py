# DFS + Memorization [Done]

# TODO DP solution
"""
DFS + Memorization
a
a

a
?

a
b*

if i == len(s) and j == len(p):
    return True

if i == len(s):
    while j < len(p):
        if * or ?
        J += 1
    if j == len(p):
    return true
    return False
if j == len(p): 
    return false

1. if s[i] == p[j] and both are regular chars: i + 1, j + 1
2. s[i] is regular char, p[j] is ?: i + 1, j + 1
3. s[i] is regular char, p[j] is *: 
    if s[i - 1] == p[j - 1] and s[i - 1] == s[i] : i + 1, j
    if [s - 1] != s[i]: i + 1, j + 1


"""
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here    
        if not p and not s:
            return True
            
        self.visited = {}
        return self.dfs(s, p, 0, 0)
        
        
    def dfs(self, s, p, s_start, p_start):
        if self.visited.get((s_start, p_start)): return self.visited.get((s_start, p_start))
    
        if p_start == len(p):
            return s_start == len(s)
        
        if s_start == len(s):
            return self.all_star(p, p_start)
                
        match = False
        if p[p_start] == '*':
            match = self.dfs(s, p, s_start + 1, p_start) or self.dfs(s, p, s_start, p_start + 1)        
        else:
            match = (p[p_start] == '?' or p[p_start] == s[s_start]) and self.dfs(s, p, s_start + 1, p_start + 1)
            
            
        self.visited[(s_start, p_start)] = match
        
        return match
        
    def all_star(self, p, p_start):
        
        while p_start < len(p) and p[p_start] == '*':
            p_start += 1
            
        return p_start == len(p)
        
        
        
        
        