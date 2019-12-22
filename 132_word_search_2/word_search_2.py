'''
=> DFS
Time: O(m * n * 4^n), m is the length of the board and n is the width of the board and n is the average length of the word
Space: O(n)
'''
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        words = set(words)
        
        rows = len(board)
        cols = len(board[0])
        
        self.res = set()
        for i in range(rows):
            for j in range(cols):
                self.dfs(board, i, j, "", words)
                    
        return list(self.res)
        
    def dfs(self, board, row, col, tmp_word, words):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#':
            return
        
        tmp_word += board[row][col]
        if tmp_word in words:
            self.res.add(tmp_word)
            
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        orig_char = board[row][col]
        board[row][col] = '#'
        for i in range(4):
            self.dfs(board, row + dx[i], col + dy[i], tmp_word, words)
        board[row][col] = orig_char

'''
=> Trie
Time: O(rows * cols * 4^l) while l is the length of the string
Space:O(26l + 4^l)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_word = True
        root.word = word
        
    def search(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root

class Solutio2:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        res = set()    
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, "", trie, res)
                
        return list(res)
        
    def dfs(self, board, row, col, tmp_word, trie, res):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#':
            return
        
        tmp_word = tmp_word + board[row][col]
        
        node = trie.search(tmp_word)
        if not node:
            return
        elif node.is_word:
            res.add(node.word)
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        orig_char = board[row][col]
        board[row][col] = '#'
        for i in range(4):
            self.dfs(board, row + dx[i], col + dy[i], tmp_word, trie, res)
        board[row][col] = orig_char

'''
=> Prefix Map
'''
class Solution3:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code 
        
        rows = len(board)
        cols = len(board[0])
        prefix_map = self.get_prefix_map(words)       
        
        self.res = set()
        for i in range(rows):
            for j in range(cols):
                self.dfs(board, i, j, "", prefix_map)
                
        return list(self.res)
    
    def get_prefix_map(self, words):
        prefix_map = {}
        
        for word in words:
            for i in range(len(word)):
                prefix = word[:i + 1]
                if prefix not in prefix_map:
                    prefix_map[prefix] = False
            prefix_map[word] = True
        
        return prefix_map
        
    def dfs(self, board, row, col, prefix, prefix_map):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#':
            return False
        
        ch = board[row][col]
        prefix += ch
        
        if prefix not in prefix_map:
            return 
        
        if prefix_map[prefix]:
            self.res.add(prefix)
            
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        board[row][col] = '#'
        for i in range(4):
            self.dfs(board, row + dx[i], col + dy[i], prefix, prefix_map)
        board[row][col] = ch
        
        return False