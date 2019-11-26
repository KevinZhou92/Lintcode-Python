class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    
    """
    2 3 1 1 4
    Greedy method for python, get maxJmp lenght at every jump, if it reaches len(A) return num of jumps.
    """
    def jump(self, A):
        # write your code here
        if len(A) == 1: return 0
        
        max_right = A[0]
        jump_count = 0
        index = 0
        next_index = 0
        
        while index < len(A):
            if max_right >= len(A) - 1:
                    break
            for i in range(index, min(len(A), max_right + 1)):
                if A[i] + i > max_right:
                    max_right = A[i] + i
                    next_index = i
                    
            if index == next_index : return -1
            index = next_index
            jump_count += 1
        
        return jump_count + 1
            
        