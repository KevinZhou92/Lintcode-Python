'''
=> Binary Seach
[4, 5, 1, 2, 3]
figure out if left or right sequence is a sorted sequence and rule out only sorted sequence
!!! Make sure we always exclude a sorted sequence, if target is not in sorted sequence, we then 
search the rest part
'''
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[end]:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
            else:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
                    
        if A[start] == target:
            return start
            
        if A[end] == target:
            return end
            
        return -1