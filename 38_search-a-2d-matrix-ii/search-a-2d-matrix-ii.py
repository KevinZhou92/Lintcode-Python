'''
=> Two Pointer
Time: O(row + col)
Space: O(1)
Note: from left bottom to upper right:
so in each row, we have ascending order
in each column, we have descending order
'''
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        rows = len(matrix)
        cols = len(matrix[0])
        
        r, c = rows - 1, 0
        count = 0
        while r >= 0 and c < cols:
            if matrix[r][c] == target:
                r -= 1 
                c += 1
                count += 1
            elif matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
                
        return count