class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        if not originalString:
            return ''
            
        res = ''
        cur_char = originalString[0]
        index = 0
        count = 0
        while index < len(originalString):
            if originalString[index] == cur_char:
                count += 1
            else:
                res += cur_char + str(count)
                count = 1
                cur_char = originalString[index]
            index += 1
        
        res += cur_char + str(count)
                
        return res if len(res) < len(originalString) else originalString