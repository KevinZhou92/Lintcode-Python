'''
=> Hashset

Time: O(nk), n arrs with k average elements
Spacs: O(k)
'''
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        res = []
        cur_set = set()
        for i in range(len(arrs)):
            if i == 0:
                cur_set = set(arrs[0])
            cur_set = cur_set & set(arrs[i])
            
        return len(cur_set)