'''
=> BFS + DFS

Note: BFS for generating distances for word transformation starting from startWord
Do dfs from end because we want to avoid unnecessary search
For example: 
start = 'a'
end = 'c'

dict = ['a', 'b', 'c]
dfs start -> end, a could search to b and c
dfs end -> start, c could only search to a

'''
from collections import deque, defaultdict
from copy import *
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        if not dict:
            return []
        
        # get pos of each word
        word_indices = self.get_word_indices(dict, start, end)
        # get possible transformations of each word
        dict = set(dict)
        dict.add(start)
        dict.add(end)
        word_map = self.get_word_map(dict)
        distances = {}
       # bfs
        self.bfs(start, end, copy(dict), word_map, distances)
        
        res = []
        # dfs(source, target, length, word_map, path, res)
        self.dfs(end, start, word_map, [end], res, distances)
        
        res.sort(key=lambda word_list: sum([word_indices[word] for word in word_list]))
        
        return res
    
    def get_word_indices(self, words, start, end):
        word_indices = {}
        for index, word in enumerate(words):
            if word not in word_indices:
                word_indices[word] = index
                
        word_indices[start] = -1
        word_indices[end] = -1
        
        return word_indices
        
    def get_word_map(self, words):
        word_map = defaultdict(set)
        for word in words:
            for i in range(len(word)):
                for j in range(ord('a'), ord('z') + 1):
                    new_word = word[:i] + chr(j) + word[i + 1:]
                    if new_word in words:
                        word_map[word].add(new_word)
                        
        return word_map
      
    def dfs(self, source, target, word_map, path, res, distances):
        if source == target:
            res.append(deepcopy(path[::-1]))
            return
        
        for neighbor in word_map[source]:
            if distances[neighbor] + 1 != distances[source]: continue
            path.append(neighbor)
            self.dfs(neighbor, target, word_map, path, res, distances)
            path.pop()
    
    def bfs(self, start, end, word_set, word_map, distances):
        queue = deque([start]) # end
        word_set -= set([start]) 
        distances[start] = 1
        length = 1
        while queue:
            size = len(queue)
            length += 1
            for _ in range(size):
                word = queue.popleft()
                distances[word] = length
                for neighbor in word_map[word]:
                    if neighbor in word_set:
                        queue.append(neighbor)
                        word_set -= set([neighbor])
                    
            