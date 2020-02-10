'''
=> Two pointers

Time: O(m + n)
Space: O(1)
'''
from heapq import *
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        res = []
        
        a, b = 0, 0
        while a < len(A) and b < len(B):
            if A[a][1] < B[b][0]:
                a += 1
            elif A[a][0] > B[b][1]:
                b += 1
            else:
                res.append([max(A[a][0], B[b][0]), min(A[a][1], B[b][1])])
                if A[a][1] > B[b][1]:
                    b += 1
                else:
                    a += 1
        return res
        