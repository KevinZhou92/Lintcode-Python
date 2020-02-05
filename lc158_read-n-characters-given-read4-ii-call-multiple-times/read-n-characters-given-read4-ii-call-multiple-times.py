"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""
class Solution:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.chunk = [''] * 4
    
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        '''
        "filetestbuffer"
        read 6 filete st
        read 5  st buf f
        read 4 f er
        '''
        index = 0
        while n > 0:
            if self.head == self.tail:
                self.tail = Reader.read4(self.chunk)
                self.head = 0
                if self.tail == 0:
                    break
            while n > 0 and self.head < self.tail:
                buf[index] = self.chunk[self.head]
                self.head += 1
                index += 1
                n -= 1
            
        return index