from collections import deque
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if not A:
            return True
            
        queue = deque([0])
        visited = set()
        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                index = queue.popleft()
                if index >= len(A) - 1: 
                    return steps
                for move in range(1, min(len(A), A[index] + 1)):
                    if index + move not in visited:
                        queue.append(index + move)
                        visited.add(index + move)
            steps += 1
            
        return -1
                        
            
            