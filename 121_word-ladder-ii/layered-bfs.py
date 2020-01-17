from collections import defaultdict, deque
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

        word_indices = self.get_word_indices(dict, start, end)
        dict = set(dict)
        dict.add(start)
        dict.add(end)
        word_map = self.get_word_map(dict)
        
        # each key is the end word of all the list in its values
        layers = {start: [[start]]}
        while layers:
            new_layers = defaultdict(list)
            for word in layers.keys():
                if word == end:
                    return sorted(layers[end], key=lambda l: sum([word_indices[w] for w in l]))
                for neighbor in word_map[word]:
                    if neighbor in dict:
                        new_layers[neighbor] += [l + [neighbor] for l in laye[word]]
            layers = new_layers
            dict -= set(new_layers.keys())
            
        return []
        
    def get_word_indices(self, words, start, end):
        word_indices = {}
        for i, v in enumerate(words):
            if v not in word_indices:
                word_indices[v] = i
                
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
        
        