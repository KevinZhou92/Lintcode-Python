'''
O(n) for min method
'''
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack:
            return -1
            
        return self.stack.pop()

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return min(self.stack)
