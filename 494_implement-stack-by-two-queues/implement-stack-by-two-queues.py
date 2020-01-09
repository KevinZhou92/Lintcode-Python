from collections import deque
class Stack:
    def __init__(self):
        self._in = deque([])
        self._out = deque([])
    
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self._in.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self._transfer()
        
        return self._out.popleft()
    
    def _transfer(self):
        while len(self._in) > 1:
            self._out.append(self._in.popleft())
            
        self._in, self._out = self._out, self._in
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        value = self.pop()
        self.push(value)
        
        return value

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self._in) == 0
