'''
=> BFS

Note:
When handle conversion betweeen list and str, must be aware of shallow copy and manipulation string 
'''
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
        
        distance = 1
        queue = deque([start])
        visited = set()
        while queue:
            size = len(queue)
            distance += 1
            for _ in range(size):
                word = queue.popleft()
                for neighbor in self.get_neighbors(word):
                    if neighbor == end:
                        return distance
                    if neighbor not in visited and neighbor in dict:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
        return 0
        
    def get_neighbors(self, word):
        import copy
        word = list(word)
        neighbors = set()
        
        for i in range(len(word)):
            tmp = copy.copy(word)
            for diff in range(26):
                replacement = chr(ord('a') + diff)
                if replacement != tmp[i]:
                    tmp[i] = replacement
                    neighbors.add(''.join(tmp))
                    
        return neighbors
        