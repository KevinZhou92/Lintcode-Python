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

    def find(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                return None
            root = root.children[char]
        
        return root.word if root.is_word else None


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


