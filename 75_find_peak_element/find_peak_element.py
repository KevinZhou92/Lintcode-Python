class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A:
            return -1
            
        start = 1
        end = len(A) - 2
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[mid + 1]:
                start = mid
            elif A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            else:
                end = mid
                
        if A[start] > A[end]:
            return start
            
        return end