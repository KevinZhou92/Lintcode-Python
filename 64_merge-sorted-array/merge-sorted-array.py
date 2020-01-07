class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if not B:
            return A
            
        a_index = m - 1
        b_index = n - 1
        
        # [1,2,3]
        # 3
        # [4,5]
        # 2
        for i in range(m + n - 1, -1, -1):
            if a_index >= 0 and b_index >= 0:
                if A[a_index] > B[b_index]:
                    A[i] = A[a_index]
                    a_index -= 1
                else:
                    A[i] = B[b_index]
                    b_index -= 1
            elif a_index >= 0:
                A[i] = A[a_index]
                a_index -= 1
            elif b_index >= 0:
                A[i] = B[b_index]
                b_index -= 1
            
                    
                