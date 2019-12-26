class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        tmp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, tmp)

    # Quick Sort
    # Time: O(NLogN), Worst O(n^2)
    # Space: O(1), in-place
    def quickSort(self, A, start, end):
        if start >= end:
            return
        
        pivot = A[start + (end - start) // 2]
        
        left, right = start, end
        
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
                
            while left <= right and A[right] > pivot:
                right -= 1
                
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
    
    # Merge Sort
    # Time: O(NlogN)
    # Space: O(N)
    # Stable 
    def mergeSort(self, A, start, end, tmp):
        if start >= end:
            return
        
        mid = start + (end - start) // 2
        self.mergeSort(A, start, mid, tmp)
        self.mergeSort(A, mid + 1, end, tmp)
        self.merge(A, start, mid, end, tmp)
       
    def merge(self, A, start, mid, end, tmp):
        l, r = start, mid + 1
        index = start
        while l <= mid and r <= end:
            if A[l] <= A[r]:
                tmp[index] = A[l]
                l += 1
            else:
                tmp[index] = A[r]
                r += 1
            index += 1
            
        while l <= mid:
            tmp[index] = A[l]
            l += 1
            index += 1
            
        while r <= end:
            tmp[index] = A[r]
            r += 1
            index += 1
            
        for i in range(start, end + 1):
            A[i] = tmp[i]

'''
[3, 2, 1, 4, 5]
2, 3
1, 4
5
'''
class Solution2:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.mergeSortBottomUp(A)
        
    def mergeSortBottomUp(self, A):
        # This represent half of number of the element that you want to sort
        size = 1
        
        while size < len(A):
            # The max index is len(A) - size + 1, imagine the moment that size is greater than
            # half of the input array, the right half won't have numbers of size, but we still need to
            # sort the right half, so as long as we have a valid mid point which is 'index + size - 1'
            # we can proceed to merge sort.
            for index in range(0, len(A) - size + 1, size * 2):
                self.merge(A, index, index + size - 1, min(index + 2 * size - 1, len(A)- 1))
            size *= 2
    
    def merge(self, A, start, mid, end):
        tmp = [0] * (end - start + 1)
        
        l, r = start, mid + 1
        index = start
        
        while l <= mid and r <= end:
            if A[l] <= A[r]:
                tmp[index - start] = A[l]
                l += 1
            else:
                tmp[index - start] = A[r]
                r += 1
            index += 1
            
        while l <= mid:
            tmp[index - start] = A[l]
            l += 1
            index += 1
            
        while r <= end:
            tmp[index - start] = A[r]
            r += 1
            index += 1
        
        for i in range(start, end + 1):
            A[i] = tmp[i - start]