import pytest
import sys
sys.path.append('.')
from util_class.Trie import Trie

def test_trie():
    word1 = 'hello'
    word2 = 'world'

    trie = Trie()
    trie.insert(word1)
    trie.insert(word2)

    assert trie.find(word1) == 'hello', "insert and find works"
    assert trie.find(word2) == 'world', "insert and find works"

if __name__ == '__main__':
    pytest.main()