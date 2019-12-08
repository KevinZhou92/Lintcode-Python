"""
1. 'e|E' presented, must have number in front and behind it
2. '+|-' can only appear after 'e|E'
3. '.' can not appear after 'e|E'
4. ' ' should not appear in string
"""

'''
http://www.cnblogs.com/grandyang/p/4084408.html
there are many cases that need to be considered:
1. space ' ': can only exist at the beginning or the end
2. dot '.': can only appear once, but it can be at front (".3") or middle(1.e2)
    or end('1.'), but it can not be after 'e/E, like 2e.1(false), 1e1.1(false)
    When it is at the end, the char before it should be digit, like "1."(true),
    "-."(false)
3. 'e/E': it must have digits before or after it, and '.' can not be after it
4. '-/+': it can only be at the begining or right after 'e', like "+1.e+5" true
'''

class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        # write your code here
        s = s.strip()
        
        num = False
        e = False
        dot = False
        num_after_e = False
        
        for index, char in enumerate(s):
            if char in '01234567890':
                num = True
                num_after_e = True
            elif char in ' \t':
                return False
            elif char in 'eE':
                if e or not num:
                    return False
                e = True
                num_after_e = False
            elif char in '-+':
                if index > 0 and s[index - 1] not in 'eE':
                    return False
            elif char in '.':
                if dot or e:
                    return False
                dot = True
            else:
                return False
        
        return num and num_after_e