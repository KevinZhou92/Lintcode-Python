'''
Use two stacks.
'''
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        # min_stack keeps track of current minimum
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if not self.min_stack or self.min_stack[-1] >= number:
            self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack:
            return -1
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        
        return self.stack.pop()

    """
    @return: An integer
    """
    # 1 1 2 3
    # 1 1 2 3
    def min(self):
        # write your code here
        return self.min_stack[-1]
