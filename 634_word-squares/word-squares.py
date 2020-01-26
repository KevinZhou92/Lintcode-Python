'''
=> DFS + Prefix Hashmap

Time: O(n^l)
'''
import copy
from collections import defaultdict
class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        '''
        # of row = # of col
        
        need n words, check if 
        
        optimization: get prefix map
        a: area
        ar: area
        l: lead, lady
        le: lead,
        wall: wall
        
        '''
        if not words:
            return []
            
        size = len(words[0])
        res = []
        prefix_map = self.get_prefix_map(words)
        self.dfs(size, prefix_map, '', [], res)

        return res
        
    def dfs(self, size, prefix_map, prefix, path, res):
        if size == len(path):
            res.append(copy.copy(path))
            return
        
        for word in prefix_map[prefix]:
            path.append(word)
            cur_size = len(path)
            if cur_size < size:
                prefix = ''.join([path[i][cur_size] for i in range(cur_size)])
                if prefix not in prefix_map:
                    path.pop()
                    continue
            self.dfs(size, prefix_map, prefix, path, res)
            path.pop()
    
    def get_prefix_map(self, words):
        prefix_map = defaultdict(set)
        
        for word in words:
            for i in range(1, len(word) + 1):
                prefix_map[word[:i]].add(word)
            prefix_map[''].add(word)
            
        return prefix_map
    
    def valid_squares(self, path, size):
        for index in range(size):
            row_word = path[index]
            col_word = ''.join([word[index] for word in path])
            if row_word != col_word:
                return False
                
        return True
        