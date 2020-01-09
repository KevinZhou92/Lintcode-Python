'''
Time: Average O(N)
'''
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.push_stack = []
        self.pop_stack = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.push_stack.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.pop_stack:
            self._transfer()
        
        return self.pop_stack.pop()

    def _transfer(self):
        while len(self.push_stack) > 0:
            self.pop_stack.append(self.push_stack.pop())
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.pop_stack:
            self._transfer() 
        
        return self.pop_stack[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0

