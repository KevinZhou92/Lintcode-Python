'''
=> Rabin-Karp
Time: O(m + n)
Space: O(1)

Note: 
For Test Case like 'aaaaaaaa', 'aaaaaa', if we caculate char value like ord(char) - ord('a'),
we will always get 0, it is not valid

Reference: https://novoland.github.io/%E7%AE%97%E6%B3%95/2014/07/26/Hash%20&%20Rabin-Karp%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%9F%A5%E6%89%BE%E7%AE%97%E6%B3%95.html
'''
class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        if target is None or source is None:
            return -1
            
        if not target:
            return 0
        
        if len(source) < len(target):
            return -1
            
        s_len = len(source)
        t_len = len(target)
        
        # MOD need to be as big as possible
        MOD = 2 ** 31
        
        target_hash = 0
        for char in target:
            target_hash = (target_hash * 31 + ord(char)) % MOD
            
        base = 1
        for i in range(len(target) - 1):
            base = (base * 31) % MOD
            
        source_hash = 0
        for i in range(s_len):
            if i >= t_len:
                source_hash = (source_hash - base * ord(source[i - t_len])) % MOD
        
            source_hash = (source_hash * 31 + ord(source[i])) % MOD
            if source_hash < 0:
                source_hash += MOD
            
            if source_hash == target_hash and self.check(source, target, i - t_len + 1):
                return i - t_len + 1
            
        return -1
        
    def check(self, source, target, index):
        t_index = 0
        while t_index < len(target) and index + t_index < len(source):
            if target[t_index] != source[index + t_index]:
                break
            t_index += 1
            
        return t_index == len(target)
        