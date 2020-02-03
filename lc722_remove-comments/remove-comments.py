class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        if not source:
            return []
        '''
        1. index of //, append if there are leading space
        2. /* 
        
        '''
        res = []
        out = ''
        block = False
        for line in source:
            index = 0
            while index < len(line):
                cur = line[index: index + 2]
                if not block and cur == '//':
                    break
                elif not block and cur == '/*':
                    block = True
                    index += 1
                elif block and cur == '*/':
                    block = False
                    index += 1
                elif not block:
                    out += cur[0]
                index += 1
            if out and not block:
                res.append(out)
                out = ''
        
        return res
    
