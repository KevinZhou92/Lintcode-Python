import string
class Solution:
    """
    @param str: the str
    @return: the letter
    """
    def findLetter(self, s):
        # Write your code here.
        if not s:
            return '~'
            
        res = '~'
        missing = set()
        for char in s:
            if char in missing and (res == '~' or res < char.upper()) :
                res = char.upper()
            elif char in string.ascii_uppercase:
                missing.add(char.lower())
            elif char in string.ascii_lowercase:
                missing.add(char.upper())
        
        return res
        