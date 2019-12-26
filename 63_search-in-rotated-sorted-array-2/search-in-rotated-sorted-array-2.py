class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return False
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[end]:
                if A[mid] <= target and target <= A[end]:
                    start = mid
                else:
                    end = mid
            elif A[mid] > A[end]:
                if A[mid] >= target and target >= A[start]:
                    end = mid
                else:
                    start = mid
            else:
                end -= 1
                    
        if A[start] == target:
            return True
            
        if A[end] == target:
            return True
        
        return False
# Time: Average O(nlogn) Worst O(n)
# Space: O(1)