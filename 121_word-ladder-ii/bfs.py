from collections import deque, defaultdict
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
        # build dict index map, used for sort res
        # bfs for word list, remove visited word
        
        word_indices = self.get_word_indices(dict, start, end)
    
        dict = set(dict)
        dict.add(start)
        dict.add(end)
        
        word_map = self.get_map(dict)
        
        queue = deque([[start]])
        found = False
        res = []
        while queue and not found:
            size = len(queue)
            visited = set()
            for _ in range(size):
                cur_list = queue.popleft()
                last_word = cur_list[-1]
                for neighbor in word_map[last_word]:
                    if neighbor == end:
                        found = True
                        new_list = cur_list + [neighbor]
                        res.append(new_list)
                    elif neighbor in dict:
                        new_list = cur_list + [neighbor]
                        visited.add(neighbor)
                        queue.append(new_list)
            dict -= visited
            
        res.sort(key=lambda word_list: sum(word_indices[word] for word in word_list))
        
        return res

    def get_word_indices(self, words, start, end):
        word_indices = {}
        for index, word in enumerate(words):
            if word in word_indices:
                continue
            word_indices[word] = index
        
        word_indices[start] = -1
        word_indices[end] = -1
        
        return word_indices

    def get_map(self, words):
        word_map = {}
        
        for word in words:
            word_map[word] = set()
            for i in range(len(word)):
                for j in range(ord('a'), ord('z') + 1):
                    new_word = word[:i] + chr(j) + word[i + 1:]
                    if new_word in words:
                        word_map[word].add(new_word)
                
        return word_map
                