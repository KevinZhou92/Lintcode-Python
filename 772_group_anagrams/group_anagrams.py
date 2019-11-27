class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        """
        eat
        nowhere
        map = {}
        for each string:
            sort string and check sorted in map, if in, put it in the list, if not create a new list
        """
        
        if not strs:
            return []
        
        group_map = {}
        
        for string in strs:
            sorted_str = str(sorted(string))
            if sorted_str not in group_map:
                group_map[sorted_str] = [string]
            else:
                group_map[sorted_str].append(string)
        
        return group_map.values()