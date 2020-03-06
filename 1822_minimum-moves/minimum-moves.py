'''
=> Two Pointer

Time: O(n)
Space: O(1)
'''
class Solution:
    """
    @param S: a string
    @return:  return the minimum number of moves
    """
    def MinimumMoves(self, S):
        # write your code here
        'baaaaa'
        'baaabbaabbba'
        if not S:
            return 0
        
        left, right = 0, 0
        min_moves = 0
        while right < len(S):
            if S[right] == S[left]:
                right += 1
            else:
                seq_len = right - left
                min_moves += seq_len // 3
                left = right
        seq_len = right - left
        min_moves += seq_len // 3
                
        return min_moves