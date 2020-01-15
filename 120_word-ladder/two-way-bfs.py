from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if not start or not end or not dict:
            return 0
            
        dict.add(end)
        
        front = set([start])
        end = set([end])
        distance = 2
        while front and end:
            front = dict & set([word[:i] + chr(replacement) + word[i + 1:] for word in front for replacement in range(ord('a'), ord('z') + 1) for i in range(len(word))])
            if front & end:
                return distance
            distance += 1
            
            # switch front and end so that we will always search the shorte set
            if len(front) > len(end):
                front, end = end, front
            # front means the word we are going to search, we will always remove these word from dict 
            # cause we don't want to visit these words again
            dict -= front
                
        return 0