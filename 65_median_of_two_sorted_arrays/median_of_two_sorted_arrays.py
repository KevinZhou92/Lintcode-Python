class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        len_A = len(A)
        len_B = len(B)
        
        if (len_A + len_B) % 2 == 1:
            return self.find_kth(A, B, 0, len_A - 1, 0, len_B - 1, (len_A + len_B) // 2 + 1)
        
        return (self.find_kth(A, B, 0, len_A - 1, 0, len_B - 1, (len_A + len_B) // 2) + self.find_kth(A, B, 0, len_A - 1, 0, len_B - 1, (len_A + len_B) // 2 + 1)) / 2
        
    def find_kth(self, A, B, A_start, A_end, B_start, B_end, k):
        if A_end < A_start:
            return B[B_start + k - 1]
            
        if B_end < B_start:
            return A[A_start + k - 1]
        
        if k == 1:
            return min(A[A_start], B[B_start])
        
        A_mid = A_start + k // 2 - 1 if A_start + k // 2 - 1 <= A_end else A_end 
        B_mid = B_start + k // 2 - 1 if B_start + k // 2 - 1 <= B_end else B_end
        
        if A[A_mid] < B[B_mid]:
            return self.find_kth(A, B, A_mid + 1, A_end, B_start, B_end, k - A_mid + A_start - 1)
        else:
            return self.find_kth(A, B, A_start, A_end, B_mid + 1, B_end, k - B_mid + B_start - 1)
        