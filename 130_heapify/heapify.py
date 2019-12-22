'''
Shift Up
Time: O(nlogn)
'''
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A)):
            self.shiftup(A, i)
            
        return A
        
    def shiftup(self, A, i):
        while i > 0:
            father = (i - 1) // 2
            if A[i] < A[father]:
                A[father], A[i] = A[i], A[father]
                i = father
            else:
                break

'''
Sink Down
Time: O(n)
'''          
class Solution2:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range((len(A) - 1) // 2, -1, -1):
            self.shift_down(A, i)
            
        return A
        
    def shift_down(self, A, i):
        while 2 * i + 1 < len(A):
            left = 2 * i + 1
            right = left + 1
            
            min_index = i
            if left < len(A) and A[left] < A[min_index]:
                min_index = left
            if right < len(A) and A[right] < A[min_index]:
                min_index = right
                
            if min_index == i:
                break
            
            A[min_index], A[i] = A[i], A[min_index]
            i = min_index