'''
=> Two Pointer
'''
class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        l, r = 0, len(num) - 1
        
        while l < r:
            if (num[l] == '6' and num[r] == '9') or (num[l] == '8' and num[r] == '8') or (num[l] == '9' and num[r] == '6') or (num[l] == '1' and num[r] == '1') or (num[l] == '0' and num[r] == '0') :
                l += 1
                r -= 1
            else:
                return False
                
        if l == r and num[l] != '0' and num[l] != '8' and num[l] != '1':
            return False
            
        return True
            
'''
=> Two Pointer Improved
'''
class Solution2:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        if not num:
            return True
        mirror = {
            '6': '9',
            '9': '6',
            '1': '1',
            '0': '0',
            '8': '8'
        }
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in mirror or num[r] not in mirror:
                return False
            if mirror[num[l]] != num[r]:
                return False
            l += 1
            r -= 1

        return True