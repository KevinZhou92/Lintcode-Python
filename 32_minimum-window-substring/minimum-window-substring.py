'''
=> Sliding Window
Time:O(n + m)
Space: O(m)
'''
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if not source or not target:
            return ''
            
        unique_chars = len(set(target))
        target_chars_map = self.get_chars_map(target)
        
        right = 0
        unique_count = 0
        chars_map = {}
        res = []
        for left in range(len(source)):
            while right < len(source) and unique_count < unique_chars:
                if source[right] in target_chars_map:
                    chars_map[source[right]] = chars_map.get(source[right], 0) + 1
                    if chars_map[source[right]] == target_chars_map[source[right]]:
                        unique_count += 1
                right += 1
            if unique_count == unique_chars:
                if not res or res[1] - res[0] > right - left:
                    res = [left, right]
            if source[left] in target_chars_map:
                chars_map[source[left]] -= 1
                if chars_map[source[left]] < target_chars_map[source[left]]:
                    unique_count -= 1
                
        return '' if not res else source[res[0]: res[1]]
    
    def get_chars_map(self, target):
        chars_map = {}
        
        for char in target:
            chars_map[char] = chars_map.get(char, 0) + 1
            
        return chars_map