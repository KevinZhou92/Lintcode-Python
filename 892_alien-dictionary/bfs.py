'''
=> BFS
Time: O(V+E)
Space: O(V+E)

Notes: 
1. It is very important to figure out the definition of the char order, we should compare between words char by char.
2. Use a minheap to output the smallest res in normal lexicographical order
'''
from heapq import *
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        indegrees, outdegrees, chars = self.get_egdes(words)
        
        heap = []
        for char in chars:
            if char not in indegrees:
                heappush(heap, char)
            
        res = []
        while heap:
            cur_char = heappop(heap)
            res.append(cur_char)
            if cur_char in outdegrees:
                for char in outdegrees[cur_char]:
                    indegrees[char] -= 1
                    if indegrees[char] == 0:
                        heappush(heap, char)
        
        return ''.join(res) if len(res) == len(chars) else ''            
                    
    def get_egdes(self, words):
        indegrees = {}
        outdegrees = {}
        chars = set()
        
        for i in range(len(words) - 1):
            for pos in range(min(len(words[i]), len(words[i + 1]))):
                prev, cur = words[i][pos], words[i + 1][pos]
                chars.add(prev)
                chars.add(cur)
                if prev != cur:
                    outdegrees[prev] = outdegrees.get(prev, []) + [cur]
                    indegrees[cur] = indegrees.get(cur, 0) + 1
            
        return indegrees, outdegrees, chars
        
                    
        
        